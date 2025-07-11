#!/usr/bin/node
const { argv } = require('node:process');

function factorial (i) {
  if (i <= 1 || isNaN(i)) {
    return (1);
  } else {
    return (i * factorial(i - 1));
  }
}

console.log(factorial(parseInt(argv[2])));
