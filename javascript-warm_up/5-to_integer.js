#!/usr/bin/node
const { argv } = require('node:process');
const fi = parseInt(argv[2]);
if (isNaN('NaN') || fi === undefined) {
  console.log('Not a number');
} else {
  console.log('My number: ' + fi);
}
