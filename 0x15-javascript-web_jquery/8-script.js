$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (info) {
  $.each(info.results, function (index, value) {
    $('#list_movies').append(value.title);
  });
});
