//fetch the characer name from URL https://swapi-api.alx-tools.com/a..
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (info) {
  $('#character').append(info.name);
});
