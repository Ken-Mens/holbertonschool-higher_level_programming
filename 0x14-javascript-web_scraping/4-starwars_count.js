#!/usr/bin/node
const request = require('request');
const check = 'https://swapi.co/api/people/18/';
let counter = 0;
const ap = process.argv[2];
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
