
$(document).ready(function(){

  $( "form" ).submit(function( event ) {

    // Stop form from submitting normally
    event.preventDefault();

    // Get some values from elements on the page:
    var $form = $( this ),
      vcontrol = $form.find( "input[name='vcontrol']" ).val(),
      vvariant = $form.find( "input[name='vvariant']" ).val(),
      cvariant = $form.find( "input[name='cvariant']" ).val(),
      ccontrol = $form.find( "input[name='ccontrol']" ).val(),
      url = $form.attr( "action" );

    var posting = $.post( url, { vcontrol: vcontrol,vvariant:vvariant,cvariant:cvariant,ccontrol:ccontrol } );

    posting.done(function( data ) {
      console.log(data)
      $("#pvalue").html(data.pvalue);
      $("#significance").html(data.significance);
      $("#result").slideDown("slow");
    });
  });

  $("#firstpanel").focusout(function(){
        if((+$("#vc").val()< +$("#vv").val()) || (+$("#vc").val() ||+$("#vv").val())<15 ){
          console.log("bad");
          $("#error1").css("display","inline").fadeOut(6000)
        }
    });

    $("#secondpanel").focusout(function(){
          if((+$("#cc").val()< +$("#cv").val()) || (+$("#cc").val() ||+$("#cv").val())<15 ){
            console.log("bad again");
            $("#error2").css("display","inline").fadeOut(6000)
          }
      });




});
