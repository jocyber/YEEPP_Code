//process the users code
function processString() {
    //function to ignore all single and double quotes - O(n)
    const input = document.getElementById("editor").innerText.replace(/"/g, '\\"');

    //send string to python
    $.ajax(
        {
            url: "{{url_for(filename='routes.py')}}",
            method: "POST",
            data: {
                name: input
            },
            success: function(response) {
                document.getElementById("editor").innerText = input;
                //show response in the output box
            }, 
            error: function(response) {
                document.getElementById("editor").innerText = input;
                //show error message in output box
            }
        }
    );
}