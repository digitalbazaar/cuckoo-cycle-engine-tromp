const cuckoo = require('cuckoo-cycle');
const benchmark = require('cuckoo-cycle/benchmark/verify');

cuckoo.engines.use('tromp', require('..'));
benchmark.run('tromp');
