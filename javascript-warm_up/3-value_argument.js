#!/usr/bin/node
const { argv } = require('node:process');
let args = argv.slice(2, 3)
if (args === null) {
  console.log('No argument');
} else {
  console.log(args);
}
