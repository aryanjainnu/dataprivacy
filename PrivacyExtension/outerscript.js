// veeeerrryy silly way of the getting all the potential html tags that the user will input info in.

for(let i = 0; i < document.querySelectorAll('input').length; i++){
    document.querySelectorAll('input')[i].addEventListener('click', ()=>{
        //Get the DOM element of whatever input user clicks on
        var currentInput = document.querySelectorAll('input')[i];
        //console.log(currentInput);

        //Just for example purposes 
        currentInput.style.color = "red";
        //document.getElementById('display').innerText = 'You clicked on input...' + (i+1);
    });
}

for(let i = 0; i < document.querySelectorAll('form').length; i++){
    document.querySelectorAll('form')[i].addEventListener('click', ()=>{
        //Get the DOM element of whatever input user clicks on
        var currentInput = document.querySelectorAll('form')[i];
        // console.log(currentInput);

        //Just for example purposes 
        currentInput.style.color = "red";
        //document.getElementById('display').innerText = 'You clicked on input...' + (i+1);
    });
}

for(let i = 0; i < document.querySelectorAll('textarea').length; i++){
    document.querySelectorAll('textarea')[i].addEventListener('click', ()=>{
        //Get the DOM element of whatever input user clicks on
        var currentInput = document.querySelectorAll('textarea')[i];
        // console.log(currentInput);

        //Just for example purposes 
        currentInput.style.color = "red";
        //document.getElementById('display').innerText = 'You clicked on input...' + (i+1);
    });
}


for(let i = 0; i < document.querySelectorAll('[contenteditable=true]').length; i++){
    document.querySelectorAll('[contenteditable=true]')[i].addEventListener('click', ()=>{
        //Get the DOM element of whatever input user clicks on
        var currentInput = document.querySelectorAll('[contenteditable=true]')[i];
        // console.log(currentInput);

        //Just for example purposes 
        currentInput.style.color = "red";
        //document.getElementById('display').innerText = 'You clicked on input...' + (i+1);
    });
}

//work on this later, might be a solution to our issues on GMAIL
// document
//     .querySelector(".body.editable.LW-avf")
//     .addEventListener('click', (e) =>{
//         e.style.color = "red";
//     })