
var recaptcha_key = "";

function gencookie(){
  function chr4(){
    return Math.random().toString(16).slice(-4);
  }
  return chr4() + chr4() + chr4() + chr4() + chr4() + chr4() + chr4() + chr4();
}
function update_status() {
    $.ajax({
            type: "GET",
            url: "/status",
            dataType: "json",
            cache: false,
            success: function(data) {
              $('#faucet-status').text(data.status)
              $('#faucet-balance').text(data.balance)
              $('#faucet-height').text(data.blocks)
            },
          });
}

function update_info() {
    $.ajax({
            type: "GET",
            url: "/info",
            dataType: "json",
            cache: false,
            success: function(data) {
              $('#faucet-address').text(data.faucet_address)
            },
          });
}


function postclaim(recaptcha_token) {

          $.ajax({
            type: "POST",
            url: "/claim",
            data: {
              _address: $('#address').val(),
              _recaptcha: recaptcha_token
            },
            dataType: "json",
            success: function(data) {
              $('#response_text').html('')
              if (data.status == 'Error') {
                 $("#response_text").removeClass().addClass("alert alert-danger");
              } else {
                 $("#response_text").removeClass().addClass("alert alert-success");
              }
              $('#response_text').html(data.msg)
            },
            error: function(data) {
              $("#response_text").removeClass().addClass("alert alert-danger");
              $('#response_text').html('Server error')
            }
          });

}


$(document).ready(function(){
   if(!Cookies.get('faucet')) {
   Cookies.set('faucet', gencookie(), {path: '' });
   }
   update_status();
   update_info();
   setInterval(update_status,30000);
   $('#claimbutton').on('click', function(e) {
          e.preventDefault();
          if(recaptcha_key != "") {
             grecaptcha.execute(recaptcha_key, {action: 'claim'}).then(function(token) {
             postclaim(token);
             });
          } else {
          postclaim('')
          }
        });
});

