#!/usr/bin/node
/* Define a function named 'add' that takes two parameters 'a' and 'b'.
 * This function computes the sum of two numbers.
 */
function add (a, b) {
  if (process.argv[2] && process.argv[3]) {
    a = Number(process.argv[2]);
    b = Number(process.argv[3]);
  }
  return a + b;
}
console.log(add());
