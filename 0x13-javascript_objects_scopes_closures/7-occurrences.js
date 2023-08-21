#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let c = 0;
  for (const element of list) {
    if (element === searchElement) {
      c += 1;
    }
  }
  return c;
};
