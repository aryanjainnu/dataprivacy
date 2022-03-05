document.addEventListener('DOMContentLoaded', function() {
    var submitButton = document.getElementById("submit-button");
    submitButton.addEventListener('click', async function(){
        var userText = document.getElementById("text-input").value;
        var redactedText = await accessAnalysis(userText);
        document.getElementById("echo").value = redactedText;
    })
})

async function accessAnalysis(userText){
    // the url might vary between systems but this is the url flask makes for me
    const response = await fetch('http://127.0.0.1:5000/',
    {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userText)
    }
    );
    return response.json();
}
