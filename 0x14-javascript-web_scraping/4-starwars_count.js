#!/usr/bin/node
// -prints the number of movies where the character “Wedge Antilles” is present.
// - use requests module

const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const peopleEndpoint = url.replace('films', 'people');
    const characterId = 18;
    let countMovie = 0;
    data.results.forEach(movie => {
      if (movie.characters.includes(`${peopleEndpoint}/${characterId}/`)) {
        countMovie++;
      }
    });
    console.log(countMovie);
  } else {
    console.log(response.statusCode);
  }
});
