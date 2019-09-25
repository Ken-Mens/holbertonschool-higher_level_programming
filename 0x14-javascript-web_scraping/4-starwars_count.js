#!/usr/bin/node
const check = 'https://swapi.co/api/people/18/';
const request = require('request');
let counter = 0;
request.get(process.argv[2], (err, res, body) => {
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
