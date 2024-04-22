#!/usr/bin/node

/**
 * Calculates the length of a string.
 * @param {string} string - The input string.
 * @returns {number} The length of the input string.
 */
function getLen (string) {
  let i = 0;
  while (string[i] !== undefined) { i++; }
  return i;
}

if (getLen(process.argv) <= 2) { console.log('No argument'); } else { console.log(process.argv[2]); }
