#!/usr/bin/node
const Square = require('./5-square.js');

module.exports = class extends Square {
  charPrint (c) {
    for (let x = 0; x < this.height; x++) {
      let arg = '';
      for (let y = 0; y < this.width; y++) { arg += c || 'X'; }
      console.log(arg);
    }
  }
};
