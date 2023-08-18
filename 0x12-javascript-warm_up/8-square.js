#!/usr/bin/node

const x = process.argv[2];

if (isNaN(x) || process.argv.length === 2) {
  console.log('Missing size');
} else if (x < 0) {
  console.log('');
} else {
  for (let i = 0; i < x; i++) {
    let str = '';
    for (let j = 0; j < x; j++) {
      str += 'X';
    }
    console.log(str);
  }
}
