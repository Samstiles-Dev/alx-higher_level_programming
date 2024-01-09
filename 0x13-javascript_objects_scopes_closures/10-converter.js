#!/usr/bin/node

exports.converter = function (base) {
  // A Function that converts a num from base 10 to another base

  return function (value) {
    return value.toString(base);
  };
};
