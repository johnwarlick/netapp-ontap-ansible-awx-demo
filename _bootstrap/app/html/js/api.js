const api_base_url = location.protocol + '//' + location.hostname + ":8000/storage/";

$(document).delegate('form', 'submit', function(e) {
    e.stopImmediatePropagation();
    e.preventDefault();
    var $form = $(this);
    type = $form.attr('id');
    // reset the status message
    $form.children('.feedback').addClass('d-none');

    // Make Form JSON Again 
    var rawdata = $form.serializeArray();
    var rawgeneral = $("#general").serializeArray();
    rawdata = rawdata.concat(rawgeneral);
    var json = {};

    $.map(rawdata, function(n, i){
        json[n['name']] = n['value'];
    });

    // Hit the right API based on request type to return job ID
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
    // don't judge me, it's been a minute
    .then(json => {
      var class_name = "danger";
      var status = parseInt(json.status);
      var message = json.message;
      var job_id = json.data;
      if(status<400 && status >=200) {
        class_name = "success";
      }
      
      // Now hit the job to get the status 
      if(parseInt(json.status) == 201) {
        // check every couple seconds until we get the success or fail
        spinner($form,true);
        fetchJobStatus(job_id, $form);
      }
    });    

});

function fetchJobStatus(id, $form) {
  fetch(api_base_url+'job/'+id)
  .then(response => response.json()) 
  .then(json => {
    var continue_poll = true;
    var class_name = "info";
    var status = parseInt(json.status);
    var message = json.message;
    var data = json.data;
    if(status == 200) {
      class_name = "success";
      continue_poll = false;
    }
    if(status >=400) {
      class_name = "danger";
      continue_poll = false;
    }
    
    console.log(status);
    console.log(message);
    console.log(data);
      
    if(continue_poll) {
      sleep(2000).then(() => {
        return fetchJobStatus(id, $form);
      });
    } else {
      spinner($form,false);
      $form.children('.feedback').removeClass('d-none')
      .addClass("alert-"+class_name).html('<p>('+status+': '+message+') '+data+'</p>'); 
    }
  });
}    

function spinner($form, present) {
  if(present) {
    $form.find('button[type="submit"] .spinner-border').removeClass('d-none');
  } else {
    $form.find('button[type="submit"] .spinner-border').addClass('d-none');
  } 

}

function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}