/**
 * Copyright (c) 2018 Digital Bazaar, Inc. All rights reserved.
 */
'use strict';

// bindings are built with a matrix of parameters
const _graphSizes = [20, 28, 30, 32];
const _edgeCounts = [8, 24, 42];
const _sipHashes = ['SipHash-2-4', 'SipHash-2-5'];
// cache of loaded bindings
const _addons = {};

function getAddon({graphSize, edgeCount, sipHash}) {
  if(!_graphSizes.includes(graphSize)) {
    throw new RangeError(`Graph size "${graphSize}" not supported.`);
  }
  if(!_edgeCounts.includes(edgeCount)) {
    throw new RangeError(`Edge count "${edgeCount}" not supported.`);
  }
  if(!_sipHashes.includes(sipHash)) {
    throw new RangeError(`Siphash "${sipHash}" not supported.`);
  }
  let sipHashName;
  if(sipHash === 'SipHash-2-4') {
    sipHashName = '2_4';
  } else if(sipHash === 'SipHash-2-5') {
    sipHashName = '2_5';
  }
  const name = `cuckoo_lean_g${graphSize}_e${edgeCount}_s${sipHashName}`;
  let addon = _addons[name];
  if(!addon) {
    addon = _addons[name] = require('bindings')(name);
  }
  return addon;
}

const api = {};
module.exports = api;

api.solve = async ({
  engine, input, graphSize, edgeCount, sipHash, nonce, maxNonces
}) => {
  const _engineOpts = typeof engine === 'string' ? {} : engine;
  const {
    threadCount = 1,
    debug = false
  } = _engineOpts;

  const addon = getAddon({graphSize, edgeCount, sipHash});
  return new Promise((resolve, reject) => {
    const opts = {
      input, graphSize, edgeCount, nonce, maxNonces, threadCount, debug
    };
    //const start = process.hrtime();
    addon.solve(opts, (err, result) => {
      if(err) {
        return reject(err);
      }
      //const diff = process.hrtime(start);
      //result.time = diff[0] + diff[1] / 1e9;
      //console.log('T', result.time);
      return resolve(result);
    });
  });
};
