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

function loginUser() {
    let email = document.getElementById("exampleInputEmail2").value;
    let password = document.getElementById("exampleInputPassword2").value;
 
    $.ajax({
        type: "POST",
        url: "/login",
        data: {"email": email, "password": password},
        success: function(data) {
            if(data === "success") {
                console.log("YESS");
                ;//set cookie, then reload page
            }
            else {
                console.log("NOOO");
                alert("No user with this email and password.")
            }
        }
    });
}

function signUpUser() {
    let email = document.getElementById("emailExample").value;
    let password = document.getElementById("passwordExample").value;
    let username = document.getElementById("usernameExample").value;

    console.log(email);

    $.ajax({
        type: "POST",
        url: "/signUp",
        data: {"email": email, "password": password, "username": username},
        success: function(data) {
            if(data === "success") {
                console.log("YESS");
                alert("SUCCESS!");
                ;//set cookie, then reload page
            }
            else {
                console.log("NOOO");
                alert("No user with this email and password.")
            }
        }
    });
}