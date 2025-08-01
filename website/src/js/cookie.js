//function to read cookies
function getCookie(name){
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

//set cookie
function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays*365*24*3600));
    let expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

window.addEventListener("DOMContentLoaded", ()=>{
    const agree = getCookie('agree');

    if(agree){
        document.getElementById('cookie-banner').style.visibility = 'hidden';
    }else{
        document.getElementById('cookie-banner').style.visibility = 'visible';
    }
})

function agree(){
    setCookie('agree', true, 1);
    document.getElementById('cookie-banner').style.visibility = 'hidden';
}
function reject(){
    document.getElementById('cookie-banner').style.visibility = 'hidden';
}