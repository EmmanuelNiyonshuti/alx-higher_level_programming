#!/usr/bin/node

/* class Square that inherits form Rectangle class */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
}
module.exports = Square;
