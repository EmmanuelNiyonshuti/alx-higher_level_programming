#!/usr/bin/node

/* get the array of the command line args and change them to Number type */
const args = process.argv.slice(2).map(Number);

/* print 0 when no args provided else sort the array in descending order and get the second index */
if (args.length === 0 || args.length === 1) { console.log(0); } else { const sortArr = args.sort((a, b) => b - a); console.log(sortArr[1]); }
