#!/usr/bin/node
const { argv } = require('node:process');
const size = parseInt(argv[2]);

if (isNaN(size) || size === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    for (let i = 0; i < size; i++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
