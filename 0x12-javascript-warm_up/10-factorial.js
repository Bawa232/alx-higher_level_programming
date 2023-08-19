#!/usr/bin/node

const length = process.argv.length;

if (length === 2 || isNaN(process.argv[2])) {
  console.log(1);
} else {
  let num = parseInt(process.argv[2]);

  for (let i = num - 1; i > 0; i--) {
    num *= i;
  }
  console.log(num);
}
