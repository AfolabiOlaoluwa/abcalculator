
$(document).ready(function(){
  $('form').submit(function(event){
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
      success: function(data){


            $('.pvalue').html(data.pvalue);
            $('#significance').html(data.significance);
            console.log(data);
        }
      // dataType : 'json',

    })
    // .done(function(data){
    //   $('#pvalue').val('').replaceWith(data.pvalue).html();
    //          $('#pvalue').html(data.pvalue);
    //          $("#significance").html(data.significance);
    //
    //
    //   console.log(data);
    // })

  });
});
