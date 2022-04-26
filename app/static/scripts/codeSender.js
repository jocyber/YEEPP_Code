function codeSend() {
    //Access code
    var code = document.getElementById("editor").value;

    $.ajax({
        type: "POST",
        url: "/parse_code",
        contentType: "application/json;",
        data: JSON.stringify({"code":code,"problem":window.location.href}),
        success: function(data) {                          //May need to change this part
            document.getElementById("codeOutput").innerHTML = data
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
            document.getElementById("numLikes").innerHTML = data.likes;
            document.getElementById("numdislikes").innerHTML = data.dislikes;
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
            document.getElementById("numdislikes").innerHTML = data.dislikes;
            document.getElementById("numLikes").innerHTML = data.likes;
        }
    });
}

function isCookie() {
    let cook = document.cookie.split("=");

    if(cook[1] != "")//if username is set
        return true;

    return false;
}

function loginUser() {
    let email = document.getElementById("exampleInputEmail2").value;
    let password = document.getElementById("exampleInputPassword2").value;

    //document.cookie = "username=" + username;
 
    $.ajax({
        type: "POST",
        url: "/login",
        data: {"email": email, "password": password},
        success: function(data) {
            if(data == "failure") {
                alert("No user with this email and password.")
            }
            else{
                document.cookie = "username=" + data;
                location.reload();
            }
        }
    });
}

function signUpUser() {
    let email = document.getElementById("emailExample").value;
    let password = document.getElementById("passwordExample").value;
    let username = document.getElementById("usernameExample").value;

    document.cookie = "username=" + username;//set cookie, then reload page

    $.ajax({
        type: "POST",
        url: "/signUp",
        data: {"email": email, "password": password, "username": username},
        success: function(data) {
            if(data === "success") {
                alert("Successfully created an account.");
            }
            else if(data === "failure") {
                alert("Could not create an account. Maybe it's already in use.");
            }
        }
    });
}

function logout() {
    document.cookie = 'username=; Max-Age=0';
    alert("Logged out successfully.");
}
