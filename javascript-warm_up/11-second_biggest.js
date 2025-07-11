#!/usr/bin/node
const { argv } = require('node:process');

function secondBiggest (i) {
  let max = i[0];
  let secMax;
  for (let x = 1; x < i.length; x++) {
    if (i[x] > max) {
      secMax = max;
      max = i[x];
    }
  }
  return secMax;
}

if (argv.length <= 3) {
  console.log(0);
} else {
  console.log(secondBiggest(argv.slice(2)));
}
