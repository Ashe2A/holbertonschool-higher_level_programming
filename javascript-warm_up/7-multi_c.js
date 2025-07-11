#!/usr/bin/node
const { argv } = require('node:process');
const occurences = parseInt(argv[2]);

if (isNaN(occurences) || occurences === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < occurences; i++) {
    console.log('C is fun');
  }
}
