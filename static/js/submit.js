function loader(){
  $('.overlay').show();
  $('.loader').show();
}

function submit() {
  formVal = $('#textbox').val().length;
  if (formVal < 1) {
    alert('No Data Supplied');
    console.log('Form data length is ' + formVal);
  } else {
    loader()
    $('#formsearch').submit();
  }
}
