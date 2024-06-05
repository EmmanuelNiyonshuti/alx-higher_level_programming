#!/usr/bin/node
// -  prints all characters of a Star Wars movie
// - Display one character name by line in the same order as the "characters" list in the /films/ response
// - use request module

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    // Create an array of promises for fetching each character
    const characterPromises = characters.map(characterUrl => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (charErr, charResponse, charBody) => {
          if (charErr) {
            reject(charErr);
          }
          if (charResponse.statusCode === 200) {
            const character = JSON.parse(charBody);
            resolve(character.name);
          } else {
            reject(new Error(`Error fetching character: ${charResponse.statusCode}`));
          }
        });
      });
    });

    // Wait for all promises to resolve
    Promise.all(characterPromises)
      .then(characterNames => {
        characterNames.forEach(name => {
          console.log(name);
        });
      })
      .catch(err => {
        console.log(err);
      });
  } else {
    console.log(`Error fetching movie: ${response.statusCode}`);
  }
});