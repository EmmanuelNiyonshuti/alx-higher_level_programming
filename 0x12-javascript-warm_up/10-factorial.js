#!/usr/bin/node
/**
 * Recursive function to calculate the factorial of a number.
 * @param {*} num The number whose factorial is to be calculated.
 * @returns The factorial of the input number.
 */
function numFactorial (num) {
  if (isNaN(num) || num === 0 || num === 1) { return (1); } else { return num * numFactorial(num - 1); }
}
const num = Number(process.argv[2]);
console.log(numFactorial(num));
