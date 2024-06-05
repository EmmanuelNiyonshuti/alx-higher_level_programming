#!/usr/bin/node
// Prints all characters of a Star Wars movie
// Displays one character name per line
// Uses the request module

const r = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

r(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characters = movie.characters;
    characters.forEach(characterUrl => {
      r(characterUrl, (charErr, charResp, charBody) => {
        if (charErr) {
          console.log(charErr);
        }
        if (charResp.statusCode === 200) {
          const character = JSON.parse(charBody);
          console.log(character.name);
        } else {
          console.log(charResp.statusCode);
        }
      });
    });
  }
});
