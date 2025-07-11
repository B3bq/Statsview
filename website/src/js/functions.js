///LOGIN
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

///ACCOUNT PAGE

//change input edit
function enableInput(inputId, confirm, cancel, change, repeat, show){
    document.getElementById(inputId).disabled = false;
    document.getElementById(confirm).hidden = false;
    document.getElementById(cancel).hidden = false;
    document.getElementById(change).hidden = true;
    document.getElementById(repeat).hidden = false;
    document.getElementById(show).hidden = false;
    if(inputId == 'input2'){    
        document.getElementById(inputId).value = "";
        document.getElementById(repeat).value = "";
    }
}

//reset values
function resetValue(inputID){
    const input = document.getElementById(inputID);
    if(inputID == 'input1'){
        input.value = input.defaultValue;
        input.disabled = true;
        document.getElementById('cancel1').hidden = true;
        document.getElementById('confirm1').hidden = true;
        document.getElementById('change1').hidden = false;
        document.getElementById('response').hidden = true;
        document.getElementById('confirm1').style.left = '50px';
    }else{
        input.value = input.defaultValue;
        input.type = 'password';
        input.disabled = true;
        document.getElementById('repeat').hidden = true;
        document.getElementById('show').hidden = true;
        document.getElementById('cancel2').hidden = true;
        document.getElementById('confirm2').hidden = true;
        document.getElementById('change2').hidden = false;
        document.getElementById('info').hidden = true;
    }
}

function passChange(){
    const pass = document.getElementById('input2').value;
    const re_pass = document.getElementById('repeat').value;
    document.getElementById('info').hidden = true;

    if(pass === re_pass){
                fetch('src/php/changepass.php', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: `password=${encodeURIComponent(pass)}`
                })
                .then(response=>response.text())
                .then(data=>{
                    if(data == 'ok'){
                        alert("Password is changed");
                        pass.value = pass.defaultValue;
                        document.getElementById('repeat').hidden = true;
                        document.getElementById('show').hidden = true;
                        document.getElementById('cancel2').hidden = true;
                        document.getElementById('confirm2').hidden = true;
                        document.getElementById('info').hidden = true;
                        document.getElementById('change2').hidden = false;
                    }else{
                        console.log(data);
                    }
                })
    }else{
        document.getElementById('info').hidden = false;
        document.getElementById('info').innerHTML = "Passwords are not the same";
    }
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

//change e-mail in account page
function changeMail(){
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const mail = document.getElementById('input1').value;
    const from = 'account';

    if(regex.test(mail)){
       window.location.href = 'verification.php?mail=' + encodeURIComponent(mail) + '&from=' + encodeURIComponent('account');
    }else{
        document.getElementById('confirm1').style.left = '-70px';
        document.getElementById('response').hidden = false;
        document.getElementById('response').innerHTML = "Invalid e-mail";
    }
}

///ACTION PAGE

//chnage name
function enableEditing(){
    document.getElementById('userName').contentEditable = true;
    document.getElementById('userName').focus();
}

///CHANGING PASS E-MAIL

//set cookie
function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays*3600));
    let expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

//page for send mail to reset pass
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
            setCookie('mail', `${mail}`, 1)
        }
        else{
            console.log(data);
        }
    })

    document.getElementById('block').style.display = 'none';
    document.getElementById('after').style.display = 'flex';
}

//changing password page after mail
function changePass(){
    const pass = document.getElementById('password').value;
    const re_pass = document.getElementById('re_password').value;

    if(pass === re_pass){
        const src = 'src/php/changepass.php';

        fetch(src, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `password=${encodeURIComponent(pass)}`
        })
        .then(response=>response.text())
        .then(data=>{
            if(data == 'ok'){
                document.getElementById('after').style.display = 'flex';
                document.getElementById('main').style.display = 'none';
                document.getElementById('head').style.display = 'none';
            }else{
                console.log(data);
            }
        })
    }else{
        document.getElementById('message').hidden = false;
        document.getElementById('message').innerText = "Passwords are not the same";
    }
}