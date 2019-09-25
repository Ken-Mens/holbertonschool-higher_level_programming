#!/usr/bin/node
const request = require('request');
let counter = 0;
request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const resp = JSON.parse(body);
    for (const x in resp.results) {
      if (resp.results[x].characters.includes('https://swapi.co/api/people/18/')) { counter++; }
    }
    console.log(counter);
  }
});
