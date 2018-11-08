/**
 * Copyright (c) 2018 Digital Bazaar, Inc. All rights reserved.
 */
'use strict';

// FIXME: update to only load bindings on demand
const addons = {
  lean_20_8: require('bindings')('cuckoo_lean_20_8'),
  lean_28_8: require('bindings')('cuckoo_lean_28_8'),
  lean_30_8: require('bindings')('cuckoo_lean_30_8'),
  lean_32_8: require('bindings')('cuckoo_lean_32_8'),

  lean_20_20: require('bindings')('cuckoo_lean_20_20'),
  lean_28_20: require('bindings')('cuckoo_lean_28_20'),
  lean_30_20: require('bindings')('cuckoo_lean_30_20'),
  lean_32_20: require('bindings')('cuckoo_lean_32_20'),

  lean_20_32: require('bindings')('cuckoo_lean_20_32'),
  lean_28_32: require('bindings')('cuckoo_lean_28_32'),
  lean_30_32: require('bindings')('cuckoo_lean_30_32'),
  lean_32_32: require('bindings')('cuckoo_lean_32_32'),

  lean_20_42: require('bindings')('cuckoo_lean_20_42'),
  lean_28_42: require('bindings')('cuckoo_lean_28_42'),
  lean_30_42: require('bindings')('cuckoo_lean_30_42'),
  lean_32_42: require('bindings')('cuckoo_lean_32_42')
};

const api = {};
module.exports = api;

api.solve = async ({
  engine, input, graphSize, edgeCount, nonce, maxNonces
}) => {
  const _engineOpts = typeof engine === 'string' ? {} : engine;
  const {
    threadCount = 1,
    debug = false
  } = _engineOpts;

  const addon = addons[`lean_${graphSize}_${edgeCount}`]
  if(!addon) {
    throw new RangeError(`Graph size of ${graphSize} not supported.`);
  }
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
