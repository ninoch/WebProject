$(function(){
  var currencies = [
    { value: 'Nazanin Alipour', data: 'AFN' },
    { value: 'Milad Asgari', data: 'ALL' },
    { value: 'Kamyar Allahverdi', data: 'DZD' },
  ];
  
  // setup autocomplete function pulling from currencies[] array
  $('#autocomplete').autocomplete({
    lookup: currencies,
    onSelect: function (suggestion) {
      var thehtml = '<strong>Currency Name:</strong> ' + suggestion.value + ' <br> <strong>Symbol:</strong> ' + suggestion.data;
      $('#outputcontent').html(thehtml);
    }
  });
  

});