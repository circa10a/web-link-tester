function submit() {
  formVal = $('#textbox').val().length;
  if (formVal < 1) {
    new Noty({text: 'No Data Supplied!',
     type: 'error',
     theme: 'mint',
      layout: 'topCenter',
     closeWith   : ['click'],
     progressBar : true,
     timeout     : 10000,
     animation   : {
      open  : 'animated bounceInDown',
      close : 'animated bounceOutUp',
      easing: 'swing',
    }
    }).show();
    console.log('Form data length is ' + formVal);
  } else {
    loader()
    $('#formsearch').submit();
  }
}
