#!/usr/bin/node
const { argv } = require('node:process');
const fi = parseInt(argv[2]);
if (isNaN(fi) || fi === undefined) {
  console.log('Not a number');
} else {
  console.log('My number: ' + fi);
}
