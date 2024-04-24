#!/usr/bin/node
/**
 * A function that logs the number of times it has been called along with the current argument value.
 * @param {*} item - The argument value to be logged.
 */
exports.logMe = function (item) {
  if (!this.count) {
    this.count = 0;
  }
  console.log(`${this.count}: ${item}`);

  this.count++;
};
