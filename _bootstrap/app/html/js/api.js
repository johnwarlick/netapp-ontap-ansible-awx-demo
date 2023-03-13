// We're just gonna pass off all the data to the API
$(document).delegate('form', 'submit', function(e) {
    e.stopImmediatePropagation();
    e.preventDefault();
    var $form = $(this);
    // add our general info with the storage type 
    var submit = $("#general").serialize();
    submit = submit+$form.serialize()+"&type="+$form.attr('id');
    console.log(submit);
    $.post( "http://localhost:8000", submit)
        .always(function(response) {
            var class_name = "danger";
            var message = "The API is currently unavailble";
            if(parseInt(response.status)==200) {
                class_name = "success";
                message = response.message;
            }
            $form.children('.feedback').removeClass('d-none')
                  .addClass("alert-"+class_name).html(message); 
        });

});