#!/usr/bin/node
const request = require('request');
let counter = 0;
request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const resp = JSON.parse(body);
    for (let x = 0; x < resp.results.length; x++) {
      for (let y = 0; y < resp.results[x].characters.length; y++) {
        if (resp.results[x].characters[y].includes('18')) { counter++; }
      }
    }
    console.log(counter);
  }
});
