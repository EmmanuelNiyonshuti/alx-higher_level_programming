#!/usr/bin/node

/* class Square that inherits form Rectangle class */

const Rectangle = require('./4-rectangle');

class BaseSquare extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = BaseSquare;
