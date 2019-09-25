#!/usr/bin/node
const request = require('request');
const obj = {};
request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const par = JSON.parse(body);
    for (const x in par) {
      if (par[x].completed) {
        if (par[x].userId in obj) { obj[par[x].userId]++; } else { obj[par[x].userId] = 1; }
      }
    }
    console.log(obj);
  }
});
