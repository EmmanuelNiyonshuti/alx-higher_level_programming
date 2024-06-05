#!/usr/bin/node
// -makes http GET request using request module
// -use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
// -prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const movieId = process.argv[2];
const endpointUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(endpointUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.log(response.statusCode);
  }
});
