function codeSend(){

    //Access code
    var code = document.getElementById("code").value;

    $.ajax({
    type: "POST",
    url: "/parse_code",
    contentType: 'application/json',
    success: function(data){                          //May need to change this part
        document.getElementById("code_output").value = data.Category[0]
        }
     });


}