#!/usr/bin/node
const x = parseInt(process.argv[2]);
function fac (x) {
  if (x < 0 || isNaN(x) || x === 0) {
    return (1);
  } else {
    return (x * fac(x - 1));
  }
}
console.log(fac(x));
