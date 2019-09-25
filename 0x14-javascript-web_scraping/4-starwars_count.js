#!/usr/bin/node
const check = 'https://swapi.co/api/people/18/';
const request = require('request');
const ap = process.argv[2];
let counter = 0;
request.get(ap, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const resp = JSON.parse(body);
    for (const x in resp.results) {
      if (resp.results[x].characters.includes(check)) { counter++; }
    }
    console.log(counter);
  }
});
