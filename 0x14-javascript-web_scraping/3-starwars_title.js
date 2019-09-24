#!/usr/bin/node
const request = require('request');
const ap = process.argv[2];
request.get('http://swapi.co/api/films/' + ap, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
