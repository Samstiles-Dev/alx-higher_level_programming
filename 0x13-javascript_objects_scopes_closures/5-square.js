#!/usr/bin/node

// A class square that defines a square and inherits 4rm Rec of 5-rectangle.js

const Rectangle = require('./4-rectangle');

// this is the class notation for defining class

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
