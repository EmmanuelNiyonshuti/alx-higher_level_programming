#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || !w || h <= 0 || !h) {
      return null;
    }
    this.width = w;
    this.height = h;
  }

  /*
    *Prints the rectangle using the character 'X'.
    */
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

  /**
   * Doubles the width and height of the rectangle.
   */
  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  /**
    * Rotates the rectangle by exchanging its width and height.
    */
  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }
}
module.exports = Rectangle;
