#!/usr/bin/node
// - comprise a script that reads and prints the content of a file

const args = process.argv;
const fs = require('fs');
fs.readFile(args[2], 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
