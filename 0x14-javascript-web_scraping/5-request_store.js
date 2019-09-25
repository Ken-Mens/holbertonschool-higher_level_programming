#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const av = process.argv[2];
const inp = process.argv[3];
request.get(av, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  fs.writeFile(inp, body, (err) => {
    if (err) console.log(err);
  });
});
