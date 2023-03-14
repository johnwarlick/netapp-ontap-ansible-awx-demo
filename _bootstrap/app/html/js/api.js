const api_base_url = location.protocol + '//' + location.hostname + ":8000";

// We're just gonna pass off all the data to the API
$(document).delegate('form', 'submit', function(e) {
    e.stopImmediatePropagation();
    e.preventDefault();
    var $form = $(this);
    // add our general info with the storage type 
    var submit = $("#general").serialize();
    submit = submit+$form.serialize()+"&type="+$form.attr('id');
    console.log(submit);
    $.post( api_base_url, submit)
        .always(function(response) {
            var class_name = "danger";
            var message = "The API is currently unavailble";
            console.log(api_base_url)
            if(parseInt(response.status)==200) {
                class_name = "success";
                message = response.message;
            }
            $form.children('.feedback').removeClass('d-none')
                  .addClass("alert-"+class_name).html(message); 
        });

});