/**
 * Copyright (c) 2018 Digital Bazaar, Inc. All rights reserved.
 */
'use strict';

const addon = require('bindings')('cuckoo');

const api = {};
module.exports = api;

api.solve = async ({
  input,
  // graph size is measured by `N` where graph is 2^N nodes
  graphSize = constants.DEFAULT_GRAPH_SIZE,
  edgeCount = constants.DEFAULT_EDGE_COUNT,
  difficulty = constants.DEFAULT_DIFFICULTY
}) => {
  addon.solve(parameters, callback);
};
