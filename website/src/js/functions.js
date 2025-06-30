function CheckUserPHP(){
    const login = document.getElementById('login').value;
    const pass = document.getElementById('password').value;
    
    let src = 'src/php/function.php';

    fetch(src, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `login=${encodeURIComponent(login)}&password=${encodeURIComponent(pass)}`
    })
    .then(response=>response.text())
    .then(data=>{
        console.log(data);
        if(data === 'OK'){
            console.log("something here");
            window.location.href = 'account.html'; // forwarding
        }
        else{
            console.log("inner");
            document.getElementById('php_result').innerHTML = data; // error message
        }
    })
}

function RememberMe(){

}