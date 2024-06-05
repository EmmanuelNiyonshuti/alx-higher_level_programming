#!/usr/bin/node
// -makes HTTP GET request using requests(it is deprecated)

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
  }
  console.log('code:', response.statusCode);
}
);
