#!/usr/bin/node
const x = (process.argv[2]);
const y = (process.argv[3]);
if (isNaN(x) || isNaN(y)) {
  console.log('NaN');
} else {
  console.log(parseInt(process.argv[2], 10) + parseInt(process.argv[3]));
}
