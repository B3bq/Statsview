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

let defaultValue = '';
//chnage name
function enableEditing(){
    const userName =  document.getElementById('userName');
    defaultValue = userName.innerText.trim();
    userName.contentEditable = true;
    userName.focus();
    document.getElementById('cancel').hidden = false;
    document.getElementById('confirm').hidden = false;
    document.getElementById('edit').hidden = true;
}

function changeName(){
    const name = document.getElementById('userName');
    let userName = name.innerText.trim();

    fetch('src/php/changename.php', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `name=${encodeURIComponent(userName)}`
    })
    .then(response=>response.text())
    .then(data=>{
        if(data == 'changed'){
            document.getElementById('cancel').hidden = true;
            document.getElementById('confirm').hidden = true;
            document.getElementById('edit').hidden = false;
            document.getElementById('userName').contentEditable = false;
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
    }else if(inputID == 'input2'){
        input.value = input.defaultValue;
        input.type = 'password';
        input.disabled = true;
        document.getElementById('repeat').hidden = true;
        document.getElementById('show').hidden = true;
        document.getElementById('cancel2').hidden = true;
        document.getElementById('confirm2').hidden = true;
        document.getElementById('change2').hidden = false;
        document.getElementById('info').hidden = true;
    }else{
        input.innerText = defaultValue;
        input.contentEditable = false;
        document.getElementById('cancel').hidden = true;
        document.getElementById('confirm').hidden = true;
        document.getElementById('edit').hidden = false;
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
function changeMail(from){
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const mail = document.getElementById('input1').value;

    if(regex.test(mail)){
       if(from == 'account'){
        fetch('src/php/verification.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `mail=${encodeURIComponent(mail)}&from=${encodeURIComponent('account')}`
           })
           .then(response=>response.text())
           .then(data=>{
            if(data == 'generate'){
                window.location.href = 'code.html?mail=' + encodeURIComponent(mail) + '&from=' + encodeURIComponent(from);
            }else{
                console.log(data);
            }
           })
       }else{
        const name = document.getElementById().value;
        const pass = document.getElementById().value;
        fetch('src/php/verification.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `mail=${encodeURIComponent(mail)}&from=${encodeURIComponent('account')}`
           })
           .then(response=>response.text())
           .then(data=>{
            if(data == 'generate'){
                window.location.href = 'code.html?mail=' + encodeURIComponent(mail) + '&from=' + encodeURIComponent(from) + '&name=' + encodeURIComponent(name) + '&pass=' + encodeURIComponent(pass);
            }else{
                console.log(data);
            }
           })
       }
    }else{
        document.getElementById('confirm1').style.left = '-70px';
        document.getElementById('response').hidden = false;
        document.getElementById('response').innerHTML = "Invalid e-mail";
    }
}

///VERIFICATION CODE
//IT FORWORD TO PHP FILE WHICH INSERT NEW USER OR UPDATE E-MAIL
function takeCode(){
    const code = document.querySelectorAll('.code');

    let userCode = '';
    code.forEach(element => {
        userCode += element.value; //merge inputs values
    });

    //taking mail from url
    let querystring = window.location.search;
    let urlParam = new URLSearchParams(querystring);
    let from = urlParam.get('from');

    if(from == 'account'){
        let mail = urlParam.get('mail');
        fetch('src/php/user.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `mail=${encodeURIComponent(mail)}&from=${encodeURIComponent(from)}&userCode=${encodeURIComponent(userCode)}`
        })
        .then(response=>response.text())
        .then(data=>{
            if(data == 'ok'){
                window.location.href = 'account.php';
            }else{
                document.getElementById('response').hidden = false;
                document.getElementById('response').innerHTML = data;
            }
        })
    }else{
        let name = urlParam.get('name');
        let pass = urlParam.get('pass');
        fetch('src/php/user.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `mail=${encodeURIComponent(mail)}&from=${encodeURIComponent(from)}&userCode=${encodeURIComponent(userCode)}&name=${encodeURIComponent(name)}&pass=${encodeURIComponent(pass)}`
        })
        .then(response=>response.text())
        .then(data=>{
            if(data == 'ok'){
                window.location.href = 'sign.html';
            }else{
                document.getElementById('response').hidden = false;
                document.getElementById('response').innerHTML = data;
            }
        })
    }
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