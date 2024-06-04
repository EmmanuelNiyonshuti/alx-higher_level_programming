#!/usr/bin/node
// -writing  a file

const f = process.argv;
const content = process.argv;
const fs = require('fs');

fs.writeFile(f[2], content[3], 'utf8', err => {
  if (err) {
    console.error(err);
  }
});
