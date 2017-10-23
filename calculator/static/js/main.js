
$(document).ready(function(){
  $('#hello').submit(function(event){
    var dataval = {
      'vcontrol' :$('input[name=vcontrol]').val(),
      'vvariant' : $('input[name=vvariant]').val(),
      'cvariant': $('input[name=cvariant]').val(),
      'ccontrol': $('input[name=ccontrol]').val()
    }
    $.ajax({
      type : 'POST',
      data : dataval,
      url : '/calculate/',
      dataType : 'json',

    })
    .done(function(data){
      //do whatever you want hee
      console.log(data)
    })
  });


});
