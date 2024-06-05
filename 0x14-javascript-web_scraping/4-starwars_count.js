#!/usr/bin/node
// -prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    let countMovie = 0;
    data.results.forEach(movie => {
      if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        countMovie++;
      }
    });
    console.log(countMovie);
  } else {
    console.log(response.statusCode);
  }
});
