#!/usr/bin/node
const request = require('request');
const fs = (process.argv[2]);
request.get(fs).on('response', res => console.log('code: ' + res.statusCode));
