#!/usr/bin/node
// -makes HTTP GET request using requests(it is deprecated)

const request = require('request');

url = process.argv[2]
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  console.log('code:', response.statusCode);
}
);
