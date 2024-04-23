#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || !w || h <= 0 || !h) {
      return null;
    }
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
