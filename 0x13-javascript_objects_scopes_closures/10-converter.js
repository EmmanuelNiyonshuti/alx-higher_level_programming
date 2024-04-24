#!/usr/bin/node
/**
 * Returns a function that converts a number from base 10 to another base.
 * @param {num} base - The base to which the number will be converted.
 * @returns {Function} - A function that accepts a number in base 10 and converts it to the specified base.
 */
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
