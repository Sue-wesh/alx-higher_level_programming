// add <li> element to a list when user clicks DIV#add_item
$('#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
