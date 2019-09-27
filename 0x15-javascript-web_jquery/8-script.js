// Queries an API and fetches all  star wars movie titles 
$.get('https://swapi.co/api/films/?format=json', function (data) {
  let films = data.results;
  for (let x of films) {
    $('ul#list_movies').append(`<li>${x.title}</li>`);
  }
});
