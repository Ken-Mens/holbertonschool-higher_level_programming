#!/usr/bin/node
const param = process.argv[2];
if (isNaN(param)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(param, 10));
}
