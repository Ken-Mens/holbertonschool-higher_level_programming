#!/usr/bin/node
exports.esrever = function (list) {
  return list.map((val, idx) => list[list.length - 1 - idx]);
};
