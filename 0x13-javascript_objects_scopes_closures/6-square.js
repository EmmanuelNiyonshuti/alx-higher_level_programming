#!/usr/bin/node

/* Defines a class that inherits from Square class and overrides print method */

const BaseSquare = require('./5-square.js');

class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
