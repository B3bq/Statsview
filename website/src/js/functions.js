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
            window.location.href = 'account.html'; // forwarding
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

export function deleteCookie(name) {
    const cookieName = encodeURIComponent(name);
    document.cookie = cookieName + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/;";
    console.log("make")
}