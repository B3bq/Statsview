function CheckUserPHP(){
    const login = document.getElementById('login').value;
    const pass = document.getElementById('password').value;
    
    let src = 'src/php/login.php';

    fetch(src, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `login=${encodeURIComponent(login)}&password=${encodeURIComponent(pass)}`
    })
    .then(response=>response.text())
    .then(data=>{
        if(data === 'OK'){
            window.location.href = 'actionpanel.html'; // forwarding
        }
        else{
            document.getElementById('php_result').innerHTML = data; // error message
        }
    })
}

function RememberMe(){
    const login = document.getElementById('login').value;
    const pass = document.getElementById('password').value;
    
    let src = 'src/php/rme.php';

    fetch(src, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `login=${encodeURIComponent(login)}&password=${encodeURIComponent(pass)}`
    })
    .then(response=>response.text())
    .then(data=>{
        if(data == "Alles klar"){
            console.log(data);
        }else{
            console.log("Error");
        }
    })
}

//change input edit
function enableInput(inputId, confirm, cancel, change, repeat){
    document.getElementById(inputId).disabled = false;
    document.getElementById(confirm).hidden = false;
    document.getElementById(cancel).hidden = false;
    document.getElementById(change).hidden = true;
    document.getElementById(repeat).hidden = false;
}

//chnage name
function enableEditing(){
    document.getElementById('userName').contentEditable = true;
    document.getElementById('userName').focus();
    document.getElementById('userName').innerHTML.replace(/<\/?u>/g, '');
}