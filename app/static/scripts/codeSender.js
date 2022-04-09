function codeSend() {
    //Access code
    var code = document.getElementById("editor").value;

    $.ajax({
    type: "POST",
    url: "/parse_code",
    contentType: 'application/json',
    data: JSON.stringify(code),
    success: function(data){                          //May need to change this part
        document.getElementById("editor").value = data
    }
    });
}