// toggle menu script
const toggleMenuEl = document.getElementById('js-toggle-menu');
const toggleableMenuEl = document.getElementById('js-toggleable-menu');
const menu = document.getElementById('menu');
let isOpen = false;

toggleMenuEl?.addEventListener('click', function(){
    toggleableMenuEl?.classList.toggle('active');
    if(isOpen){
        menu.src = "src/img/burger-bar.png";
    }
    else{
        menu.src = "src/img/arrow.png";
    }
    isOpen = !isOpen; // change condition
})

const breakpoint = window.matchMedia('(min-width: 768px)');
breakpoint.addEventListener('change', function(){
    toggleableMenuEl?.classList.remove('active');
})

// Getting cookies values
//function to read cookies
function getCookie(name){
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

//deleting cookies
function deleteCookie(name) {
    const cookieName = encodeURIComponent(name);
    document.cookie = cookieName + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/;";
}

//visible summary button
function visibleSummary(){
    // list of allowed dates in "MM-DD" format
    const allowedDates = [
        "07-06",
        "07-15",
        "07-16",
        "07-17",
        "07-18",
        "01-01",
        "01-02",
        "01-03",
        "01-04",
    ];

    // get today date
    const today = new Date();
    const mm = String(today.getMonth()+1).padStart(2, '0');
    const dd = String(today.getDate()).padStart(2, '0');
    const todayString = `${mm}-${dd}`;

    // show or hidden button
    const summaryBtn = document.getElementById('summary');
    if(allowedDates.includes(todayString)){
        summaryBtn.style.display = "inline-block";
    }else{
        summaryBtn.style.display = "none";
    }
}

//listening
window.addEventListener('DOMContentLoaded', ()=>{
    const userID = getCookie("user"); //user id
    const userName = getCookie("name"); //user name
    console.log(document.cookie);

    if(userID){
        document.getElementById('option1').innerHTML = "My account";
        document.getElementById('option1').title = "My account";
        document.getElementById('option1').href = "account.php";
        document.getElementById('option2').innerHTML = "Action panel";
        document.getElementById('option2').title = "Action panel";
        document.getElementById('option2').href = "actionpanel.html";
        document.getElementById('logout').innerHTML = "Log out";
        document.getElementById('logout').title = "Log out";
        document.getElementById('logout').onclick = ()=>{
            deleteCookie('user');
            deleteCookie('name');
        };
        document.getElementById('userName').innerText = `${userName}`;

        visibleSummary(); //visibility summary nutton
    }
})

// script to show password
const pass = document.getElementById('password');
const re_pass = document.getElementById('re_password');
const show_pass = document.getElementById('show_password');

show_pass.addEventListener('change', function(){
    pass.type = this.checked ? 'text' : 'password';
    re_pass.type = this.checked ? 'text' : 'password';
});