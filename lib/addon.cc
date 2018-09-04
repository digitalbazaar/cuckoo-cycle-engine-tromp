/*********************************************************************
 * NAN - Native Abstractions for Node.js
 *
 * Copyright (c) 2017 NAN contributors
 *
 * MIT License <https://github.com/nodejs/nan/blob/master/LICENSE.md>
 ********************************************************************/

#include <nan.h>
//#include "addon.h"   // NOLINT(build/include)
#include "pow.h"  // NOLINT(build/include)

using Nan::AsyncQueueWorker;
using Nan::AsyncWorker;
using Nan::Callback;
using Nan::GetFunction;
using Nan::HandleScope;
using Nan::New;
using Nan::Null;
using Nan::Set;
using Nan::To;
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
      const unsigned graphSize,
      const unsigned edgeCount,
      Callback *callback)
      : AsyncWorker(callback), graphSize(graphSize), edgeCount(edgeCount)) {
        memcpy(this->input, input, 32);
      }
    ~SolutionWorker() {}

    // Executed inside the worker-thread.
    // It is not safe to access V8, or V8 data structures
    // here, so everything we need for input and output
    // should go on `this`.
    void Execute () {
      // TODO: do things
      Equihash equihash(n, k, seed);
      Proof p = equihash.FindProof();
      solution = p.inputs;
      nonce = p.nonce;
      //printhex("solution", &solution[0], solution.size());
    }

    // Executed when the async work is complete
    // this function will be run inside the main event loop
    // so it is safe to use V8 again
    void HandleOKCallback () {
      // TODO: do things
      HandleScope scope;
      Local<Object> obj = Nan::New<Object>();
      Local<Object> proofValue =
        Nan::CopyBuffer((const char*)&solution[0], solution.size() * 4)
          .ToLocalChecked();

       //printhex("solution COPY", &solution[0], solution.size());

      obj->Set(New("n").ToLocalChecked(), New(n));
      obj->Set(New("k").ToLocalChecked(), New(k));
      obj->Set(New("nonce").ToLocalChecked(), New(nonce));
      obj->Set(New("value").ToLocalChecked(), proofValue);

      Local<Value> argv[] = {
        Null(),
        obj
      };

      callback->Call(2, argv);
    }

  private:
    unsigned char input[32];
    unsigned graphSize;
    unsigned edgeCount;
    // TODO: do things
    std::vector<Input> solution;
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
   Handle<Value> nValue = object->Get(New("n").ToLocalChecked());
   Handle<Value> kValue = object->Get(New("k").ToLocalChecked());
   Handle<Value> input = object->Get(New("input").ToLocalChecked());

   const unsigned n = To<uint32_t>(nValue).FromJust();
   const unsigned k = To<uint32_t>(kValue).FromJust();
   size_t bufferLength = node::Buffer::Length(input) / 4;
   unsigned* input = (unsigned*)node::Buffer::Data(input);

   //printhex("seed", seedBuffer, bufferLength);

   Seed seed(seedBuffer, bufferLength);

   AsyncQueueWorker(new SolutionWorker(n, k, seed, callback));
}

NAN_MODULE_INIT(InitAll) {
  Set(target, New<String>("solve").ToLocalChecked(),
    GetFunction(New<FunctionTemplate>(Solve)).ToLocalChecked());
}

NODE_MODULE(addon, InitAll)
