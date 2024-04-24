#!/usr/bin/node

/**
 * Calculates the length of a string since  the requirement says we'are not allowed to use length.
 * @param {string} string - The input string.
 * @returns {number} The length of the input string.
 */
function getLen (string) {
  let i = 0;
  while (string[i] !== undefined) { i++; }
  return i;
}

if (getLen(process.argv) <= 2) { console.log('No argument'); } else { console.log(process.argv[2]); }

// Simpler approach

// if (!process.argv.slice(2)[0]) {
//   console.log('No argument');
// }
// else {
//   console.log(process.argv.slice(2)[0]);
// }
