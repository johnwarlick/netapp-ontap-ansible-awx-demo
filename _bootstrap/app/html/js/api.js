const api_base_url = location.protocol + '//' + location.hostname + ":8000";

// We're just gonna pass off all the data to the API
$(document).delegate('form', 'submit', function(e) {
    e.stopImmediatePropagation();
    e.preventDefault();
    var $form = $(this);
    type = $form.attr('id');
    (async () => {
        //const response = await fetch(api_base_url+'/test', {
        const response = await fetch(api_base_url+'/storage/'+type, {
          method: 'POST',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          mode: "cors",
          credentials: "same-origin",
          body: JSON.stringify({name: "Test", size: 1.25, unit: 'tb', protocol: 'cifs'})
        });
        const resp = await response;
        console.log(resp);
        var status = parseInt(resp.status);
        var message = resp.statusText;
        var body = resp.body;
        var class_name = "success";
        if (status >=400) {
            class_name = "danger";
        }
        $form.children('.feedback').removeClass('d-none')
            .addClass("alert-"+class_name).html(status+': '+message); 
    })();
    // var $form = $(this);
    // // add our general info with the storage type 
    // var submit = $("#general").serialize();
    // submit = submit+'&'+$form.serialize();
    // type = $form.attr('id');
    // console.log(submit);
    // $.post({
    //     url: api_base_url+'/storage/'+type, 
    //     data: submit, 
    //     dataType: 'json',
    // }).always(function(response) {
    //     var class_name = "danger";
    //     console.log(response);
    //     message = response.statusText;
    //     var status = parseInt(response.status);
    //     // var message = "The API is currently unavailble";
    //     // if(response.message) {
    //     //     message = response.message;
    //     // }
    //     // if(status==200) {
    //     //     class_name = "success";
    //     // }
    //     $form.children('.feedback').removeClass('d-none')
    //             .addClass("alert-"+class_name).html(status+': '+message); 
    // });

});