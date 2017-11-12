function validateURL() {
if(/^(http|https|ftp):\/\/[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$/i.test($("#textbox").val())){
    alert("valid URL");
    loader()
} else {
  new Noty({text: 'Invalid URL!',
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
  return false
  }
}
