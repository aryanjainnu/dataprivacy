document.addEventListener('DOMContentLoaded', function() {
    var submitButton = document.getElementById("submit-button");
    submitButton.addEventListener('click', async function(){
        var x = document.getElementById("text-input").value;
        // WE WILL DO SOMETHING COOL WITH THE VALUE, RN JUST IS THE DOGGY EXAMPLE
        var stuff = await accessAnalysis(x)
        // document.getElementById("echo").value = exampleFunction(x);
        document.getElementById("echo").value = stuff;
    })
})

function exampleFunction(x) {
    return x.replace(/dog/g, "precious boi");
}

async function accessAnalysis(text){
    const response = await fetch('http://127.0.0.1:5000/',
    {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(text)
    }
    );
    return response.json();
}
