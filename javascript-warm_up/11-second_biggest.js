#!/usr/bin/node
const { argv } = require('node:process');
const args = argv.slice(2);

function compareNumbers (a, b) {
  return a - b;
}

function secondBiggest (i) {
  i.sort(compareNumbers);
  console.log(i[i.length - 2]);
}

if (args.length <= 1) {
  console.log(0);
} else {
  secondBiggest(args);
}
