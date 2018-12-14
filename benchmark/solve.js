const cuckoo = require('cuckoo-cycle');
const benchmark = require('cuckoo-cycle/benchmark/solve');

cuckoo.engines.use('tromp', require('..'));
benchmark.run('tromp');
