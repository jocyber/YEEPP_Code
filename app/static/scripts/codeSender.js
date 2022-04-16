function codeSend() {
    //Access code
    var code = document.getElementById("editor").value;

    $.ajax({
        type: "POST",
        url: "/parse_code",
        contentType: 'application/json',
        data: JSON.stringify(code),
        success: function(data) {                          //May need to change this part
            document.getElementById("editor").value = data
            //for outputing the code results
            //document.getElementById("codeOutput").innerHTML = code; code would be a return variable
        }
    });
}

function updateLike() {
    let id = document.getElementById("like").value;

    $.ajax({
        type: "POST",
        url: "/update_count",
        data: {"data": "like", "id": id},
        success: function(data) {
            document.getElementById("numLikes").innerHTML = data;
        }
    });
}

function updateDislike() {
    let id = document.getElementById("dislike").value;

    $.ajax({
        type: "POST",
        url: "/update_count",
        data: {"data": "dislike", "id": id},
        success: function(data) {
            document.getElementById("numdislikes").innerHTML = data;
        }
    });
}