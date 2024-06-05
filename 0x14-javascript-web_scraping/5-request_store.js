#!/usr/bin/node
// - gets the contents of a webpage and stores it in a file.
// - use request module

const r = require('request');
const fs = require('fs');

const url = process.argv[2];
const f = process.argv[3];

r(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode === 200) {
    fs.writeFile(f, body, 'utf-8', err => {
      if (err) {
        console.error(err);
      }
    });
  } else {
    console.log(response.statusCode);
  }
});
