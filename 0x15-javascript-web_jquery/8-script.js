/*
JavaScript script that fetches and
lists the title for all movies
by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
*/

$(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, function (response) {
    const movies = response.results;
    movies.forEach(movie => {
      $('#list_movies').append(`<li>${movie.title}</li>`);
    });
  }, 'json');
});
