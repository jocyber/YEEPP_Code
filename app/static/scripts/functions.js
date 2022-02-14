//using jQuery frontend framework
$(document).ready(function()  {

    //process the users code
    $("#code_form").submit(function (e) {
        //function to ignore all single and double quotes - O(n)
        console.log("success");
        let input = $("editor").innerText;//.replace(/\"/g, '\\"');

        //send string to python
        $.ajax(
            {
                url: "/test",
                method: "POST",
                data: {
                    name: input
                },
                success: function(response) {
                    $("editor").innerText = response;
                    //show response in the output box
                }, 
                error: function(response) {
                    document.getElementById("editor").innerText = input;
                    //show error message in output box
                }
            }
        );

        e.preventDefault();//prevent html for submitting form data more than once
    });
});