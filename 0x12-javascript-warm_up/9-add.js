#!/usr/bin/node

const num = process.argv.length;
const i = process.argv[2];
const j = process.argv[3];

if (num < 4 || isNaN(i) || isNaN(j)) {
  console.log('NaN');
} else {
  console.log(parseInt(i) + parseInt(j));
}
