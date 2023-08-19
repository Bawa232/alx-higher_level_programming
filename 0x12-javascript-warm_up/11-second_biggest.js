#!/usr/bin/node

const args = process.argv.slice(2);
const length = process.argv.length;

if (length < 4) {
  console.log(0);
} else {
  const arr = args.map(Number);
  const large = Math.max(...arr);
  const arr2 = arr.filter(num => num !== large);
  const large2 = Math.max(...arr2);

  console.log(large2);
}
