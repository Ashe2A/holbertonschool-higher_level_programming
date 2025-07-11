#!/usr/bin/node
const { argv } = require('node:process');
const args = argv.slice(2);

function secondBiggest (i) {
  let max = i[0];
  let secMax;
  for (let x = 1; x < i.length; x++) {
    if (i[x] > max) {
      secMax = max;
      max = i[x];
    }
  }
  console.log(secMax);
}

if (argv.length <= 3) {
  console.log(0);
} else {
  secondBiggest(args);
}
