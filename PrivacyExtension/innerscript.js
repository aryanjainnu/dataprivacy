document.addEventListener('DOMContentLoaded', addEvent)

function addEvent() {
    var textArea = document.getElementById("text-input");
    textArea.addEventListener("keyup", async function(){
        var redactedText = await findPII(textArea.textContent);
        document.getElementById("echo").value= redactedText;
        //will use innerHTML in the future so that text can highlight when algo finds that its sensitive information
        //document.getElementById("text-input").innerHTML= `<mark>oh noes!</mark>`;
    });
}

async function findPII(userText){
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

