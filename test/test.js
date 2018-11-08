const assert = require('assert');
const cuckoo = require('cuckoo-cycle');
const engineTest = require('cuckoo-cycle/test/engine');

cuckoo.engines.use('tromp', require('..'));

describe('cuckoo engine tromp', function() {
  engineTest.createTests('tromp');
});
