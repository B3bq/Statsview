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
function enableInput(inputId, confirm, cancel, change, repeat, show){
    document.getElementById(inputId).disabled = false;
    document.getElementById(confirm).hidden = false;
    document.getElementById(cancel).hidden = false;
    document.getElementById(change).hidden = true;
    document.getElementById(repeat).hidden = false;
    document.getElementById(show).hidden = false;
}

let isOpen = true;
//show password
function showPassword(show, input2, repeat){
    if(isOpen){
        document.getElementById(show).src = "src/img/show.png";
        document.getElementById(input2).type = "text";
        document.getElementById(repeat).type = "text";
    }else{
        document.getElementById(show).src = "src/img/hide.png";
        document.getElementById(input2).type = "password";
        document.getElementById(repeat).type = "password";
    }
    isOpen = !isOpen;
}

//chnage name
function enableEditing(){
    document.getElementById('userName').contentEditable = true;
    document.getElementById('userName').focus();
}

function passReset(){
    const mail = document.getElementById('email').value;

    const src = 'src/php/resetpass.php';

    fetch(src, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `mail=${encodeURIComponent(mail)}`
    })
    .then(response=>response.text())
    .then(data=>{
        if(data === "sent"){
            
        }
        else{
            console.log(data);
        }
    })

    document.getElementById('block').style.display = 'none';
    document.getElementById('after').style.display = 'flex';
}