$(document).ready(function(){
    $('.details').click(function(event){
        event.preventDefault();
        var id = $(this).attr('href');
          $.ajax({
             url: id,
             success: function(data){
                 alert(data);
             },
             error: function(){
               alert('failure');
             }
        });



    })
});








