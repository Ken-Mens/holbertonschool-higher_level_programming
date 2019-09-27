// Fetches and replaces the name of API data and replaces name
$.get('https://swapi.co/api/people/5/?format=json', function (data, stat) {
    $('div#character').text(data.name);
});
