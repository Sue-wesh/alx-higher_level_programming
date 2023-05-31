// fetch from URL and display the value of hello from that fetch in DIV#hello
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (info) {
  $('#hello').append(info.hello);
});
