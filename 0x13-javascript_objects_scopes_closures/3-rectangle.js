#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || !w || h <= 0 || !h) {
      return null;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let j = 0;
    while (j < this.height) {
      let str = '';
      for (let i = 0; i < this.width; i++) {
        str += 'X';
      }
      console.log(str);
      j++;
    }
  }
}
module.exports = Rectangle;
