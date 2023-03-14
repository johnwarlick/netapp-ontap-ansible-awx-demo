const api_base_url = location.protocol + '//' + location.hostname + ":8000/storage/";

$(document).delegate('form', 'submit', function(e) {
    e.stopImmediatePropagation();
    e.preventDefault();
    var $form = $(this);
    type = $form.attr('id');

    // Make Form JSON Again 
    var rawdata = $form.serializeArray();
    var rawgeneral = $("#general").serializeArray();
    rawdata = rawdata.concat(rawgeneral);
    var json = {};

    $.map(rawdata, function(n, i){
        json[n['name']] = n['value'];
    });

    // Hit the right API based on request type
    fetch(api_base_url+type, {
      method: "post",
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },    
      mode: "cors",
      credentials: "same-origin",
      body: JSON.stringify(json),
    })
    .then(response => response.json()) 
    // Look the javascript is not the point of this demo ok, 
    // don't judge me
    .then(json => {
      var class_name = "danger";
      var status = parseInt(json.status);
      var message = json.message;
      var response = json.data;
      if(status<400 && status >=200) {
        class_name = "success";
      }
      $form.children('.feedback').removeClass('d-none')
          .addClass("alert-"+class_name).html(status+': '+message+'<br/>'+response); 
    });    
});