#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occur = 0;
  for (let x = 0; x < list.length; x++) {
    if (list[x] === searchElement) {
      occur = occur + 1;
    }
  }
  return occur;
};
