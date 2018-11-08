const cuckoo = require('cuckoo-cycle');
const benchmark = require('cuckoo-cycle/benchmark/nonces');

cuckoo.engines.use('tromp', require('..'));

const engine = 'tromp';

// easiest difficulty
const DIFFICULTY_1X = Buffer.allocUnsafe(32).fill(0xFF);
const DIFFICULTY_2X = Buffer.from(DIFFICULTY_1X);
DIFFICULTY_2X[0] = 0x7F;
const DIFFICULTY_4X = Buffer.from(DIFFICULTY_1X);
DIFFICULTY_4X[0] = 0x3F;
const DIFFICULTY_8X = Buffer.from(DIFFICULTY_1X);
DIFFICULTY_8X[0] = 0x1F;
const DIFFICULTY_16X = Buffer.from(DIFFICULTY_1X);
DIFFICULTY_16X[0] = 0x0F;

async function _g20_e42_threads() {
  const graphSize = 20;
  const edgeCount = 42;
  const count = 100;

  // thread count tests
  for(let tc of [4,8]) {
    await benchmark.findNonces({
      engine: {name: engine, threadCount: tc}, graphSize, edgeCount,
      tag: 't' + tc, count});
  }
};

async function _gX_e42() {
  const edgeCount = 42;
  const count = 20;

  await benchmark.findNonces({
    engine: {name: engine}, graphSize: 20, edgeCount, count});
  await benchmark.findNonces({
    engine: {name: engine}, graphSize: 28, edgeCount, count});
  await benchmark.findNonces({
    engine: {name: engine}, graphSize: 30, edgeCount, count});
};

async function _g_eX({graphSize}) {
  const count = 20;

  await benchmark.findNonces({
    engine: {name: engine}, graphSize, edgeCount: 8, count});
  await benchmark.findNonces({
    engine: {name: engine}, graphSize, edgeCount: 20, count});
  await benchmark.findNonces({
    engine: {name: engine}, graphSize, edgeCount: 32, count});
  await benchmark.findNonces({
    engine: {name: engine}, graphSize, edgeCount: 42, count});
};

async function _g_eX({graphSize}) {
  const count = 20;

  await benchmark.findNonces({
    engine: {name: engine}, graphSize, edgeCount: 8, count});
  await benchmark.findNonces({
    engine: {name: engine}, graphSize, edgeCount: 20, count});
  await benchmark.findNonces({
    engine: {name: engine}, graphSize, edgeCount: 32, count});
  await benchmark.findNonces({
    engine: {name: engine}, graphSize, edgeCount: 42, count});
};

async function _g_e_dX({graphSize, edgeCount}) {
  const count = 50;

  await benchmark.findNonces({
    engine: {name: engine}, graphSize, edgeCount, difficulty: DIFFICULTY_1X,
    count, tag: '1x'});
  await benchmark.findNonces({
    engine: {name: engine}, graphSize, edgeCount, difficulty: DIFFICULTY_2X,
    count, tag: '2x'});
  await benchmark.findNonces({
    engine: {name: engine}, graphSize, edgeCount, difficulty: DIFFICULTY_4X,
    count, tag: '4x'});
  await benchmark.findNonces({
    engine: {name: engine}, graphSize, edgeCount, difficulty: DIFFICULTY_8X,
    count, tag: '8x'});
  await benchmark.findNonces({
    engine: {name: engine}, graphSize, edgeCount, difficulty: DIFFICULTY_16X,
    count, tag: '16x'});
};

async function run() {
  //await _g20_e42();
  //await _gX_e42();
  //await _g_eX({graphSize: 20});
  //await _g_eX({graphSize: 28});
  await _g_e_dX({graphSize: 20, edgeCount: 8});
};

run();
