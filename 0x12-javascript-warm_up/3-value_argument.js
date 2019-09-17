#!/usr/bin/node
const Count = process.argv[2];
if (!Count) {
  console.log('No argument');
} else {
  console.log(Count);
}
