/*********************************************************************
 * Cuckoo Cycle native bindings for Node.js
 *
 * Copyright (c) 2018 Digital Bazaar, Inc.
 *
 * MIT License <https://github.com/nodejs/nan/blob/master/LICENSE.md>
 ********************************************************************/

#include <nan.h>
//#include "addon.h"   // NOLINT(build/include)
#include "cuckoo/src/cuckatoo/lean.hpp"  // NOLINT(build/include)

// FIXME: from lean_miner
//#define MAXSOLS 8
// FIXME: find better way to calculate ntrims
//#define PART_BITS 0
// FIXME
#define HEADERLEN 80

using Nan::AsyncQueueWorker;
using Nan::AsyncWorker;
using Nan::Callback;
using Nan::GetFunction;
using Nan::HandleScope;
using Nan::New;
using Nan::Null;
using Nan::Set;
using Nan::To;
using v8::Array;
using v8::Function;
using v8::FunctionTemplate;
using v8::Handle;
using v8::Isolate;
using v8::Local;
using v8::Number;
using v8::Object;
using v8::String;
using v8::Value;

class SolutionWorker : public AsyncWorker {
  public:
    SolutionWorker(
      const unsigned char* input,
      const size_t inputLength,
      const unsigned graphSize,
      const unsigned edgeCount,
      const unsigned nonce,
      const unsigned maxNonces,
      const unsigned threadCount,
      const bool debug,
      Callback *callback)
      : AsyncWorker(callback),
      inputLength(inputLength),
      graphSize(graphSize),
      edgeCount(edgeCount),
      nonce(nonce),
      maxNonces(maxNonces),
      threadCount(threadCount),
      debug(debug) {
      memcpy(this->input, input, inputLength);
    }
    ~SolutionWorker() {}

    // Executed inside the worker-thread.
    // It is not safe to access V8, or V8 data structures
    // here, so everything we need for input and output
    // should go on `this`.
    void Execute () {
      /*
      unsigned ntrims = 1 + (PART_BITS+3)*(PART_BITS+4)/2;
      nsols = 0;
      solutions.resize(MAXSOLS * PROOFSIZE);
      //printf("EXE t:%d t:%d n:%d m:%d\n", nthreads, ntrims, nonce, maxNonces);
      lean_miner(
        threadCount, ntrims,
        nonce, maxNonces,
        (char *)input, inputLength,
        &solutions[0], nonces, &nsols,
        debug);
      */
       memset(header, 0, sizeof(header));
       memcpy(header, input, inputLength);
       SolverParams params;
       fill_default_params(&params);
       params.nthreads = threadCount;
       //params.ntrims = ;
       SolverCtx *ctx = create_solver_ctx(&params);
       //run_solver(ctx, (char *)input, inputLength, nonce, maxNonces, &solutions, &stats);
       run_solver(ctx, header, sizeof(header), nonce, maxNonces, &solutions, &stats);
       destroy_solver_ctx(ctx);
    }

    // Executed when the async work is complete
    // this function will be run inside the main event loop
    // so it is safe to use V8 again
    void HandleOKCallback () {
      // result is of format:
      // {
      //   solutions: [ { nonce: ..., edges: ...}, ... ]
      // }
      HandleScope scope;
      Local<Object> result = Nan::New<Object>();
      //Local<Array> solutions = New<v8::Array>(nsols);
      Local<Array> solutions = New<v8::Array>(this->solutions.num_sols);
      result->Set(New("solutions").ToLocalChecked(), solutions);
      /*
      printf("S[%d]:", nsols);
      for(unsigned z = 0; z < PROOFSIZE * MAXSOLS; ++z) {
        printf(" %d", this->solutions[z]);
      }
      printf("\n");
      */

      for(unsigned s = 0; s < this->solutions.num_sols; ++s) {
        Local<Object> solution = Nan::New<Object>();
        Local<Array> edges = New<v8::Array>(PROOFSIZE);
        for(unsigned i = 0; i < PROOFSIZE; ++i) {
          //Set(edges, i, New(this->solutions[(s * PROOFSIZE) + i]));
          Set(edges, i, New((uint32_t)this->solutions.sols[s].proof[i]));
        }

        //solution->Set(New("nonce").ToLocalChecked(), New(nonces[s]));
        solution->Set(New("nonce").ToLocalChecked(), New((uint32_t)this->solutions.sols[s].nonce));
        solution->Set(New("edges").ToLocalChecked(), edges);
        Set(solutions, s, solution);
      }

      Local<Value> argv[] = {
        Null(),
        result
      };

      callback->Call(2, argv);
    }

  private:
    char header[HEADERLEN];
    unsigned char input[32];
    size_t inputLength;
    unsigned graphSize;
    unsigned edgeCount;
    unsigned nonce;
    unsigned maxNonces;
    unsigned threadCount;
    unsigned nsols;
    bool debug;
    //std::vector<uint32_t> solutions;
    //unsigned nonces[MAXSOLS];
    SolverSolutions solutions;
    SolverStats stats;
};

NAN_METHOD(Solve) {
   // ensure first argument is an object
   if(!info[0]->IsObject()) {
      Nan::ThrowTypeError("'options' must be an object");
      return;
   }
   // ensure second argument is a callback
   if(!info[1]->IsFunction()) {
      Nan::ThrowTypeError("'callback' must be a function");
      return;
   }

   Callback *callback = new Callback(info[1].As<Function>());
   Handle<Object> object = Handle<Object>::Cast(info[0]);
   Handle<Value> inputValue =
      object->Get(New("input").ToLocalChecked());
   Handle<Value> graphSizeValue =
      object->Get(New("graphSize").ToLocalChecked());
   Handle<Value> edgeCountValue =
      object->Get(New("edgeCount").ToLocalChecked());
   Handle<Value> nonceValue =
      object->Get(New("nonce").ToLocalChecked());
   Handle<Value> maxNoncesValue =
      object->Get(New("maxNonces").ToLocalChecked());
   Handle<Value> threadCountValue =
      object->Get(New("threadCount").ToLocalChecked());
   Handle<Value> debugValue =
      object->Get(New("debug").ToLocalChecked());

   unsigned char* input = (unsigned char*)node::Buffer::Data(inputValue);
   size_t inputLength = node::Buffer::Length(inputValue);
   const unsigned graphSize = To<uint32_t>(graphSizeValue).FromJust();
   const unsigned edgeCount = To<uint32_t>(edgeCountValue).FromJust();
   const unsigned nonce = To<uint32_t>(nonceValue).FromJust();
   const unsigned maxNonces = To<uint32_t>(maxNoncesValue).FromJust();
   const unsigned threadCount = To<uint32_t>(threadCountValue).FromJust();
   const bool debug = To<bool>(debugValue).FromJust();

   AsyncQueueWorker(new SolutionWorker(
      (unsigned char*)input, inputLength, graphSize, edgeCount, nonce,
      maxNonces, threadCount, debug, callback));
}

NAN_MODULE_INIT(InitAll) {
  Set(target, New<String>("solve").ToLocalChecked(),
    GetFunction(New<FunctionTemplate>(Solve)).ToLocalChecked());
}

NODE_MODULE(addon, InitAll)
