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
        "07-20",
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
    const paths = ['/account.php', '/actionpanel.html'];
    const currentPath = window.location.pathname;
    const isPath = paths.some(path => currentPath.endsWith(path));

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
    }else if(isPath && !userID){ //when path is in account or action panel and doesn't exist cookie
        window.location.href = 'login.html';
    }
})

const inputs = document.querySelectorAll(".code");

inputs.forEach((input, index)=>{
    input.addEventListener("input", ()=>{
        if(input.value.length === 1 && index < inputs.length -1){
            inputs[index+1].focus();
        }
    });

    input.addEventListener("keydown",(e)=>{
        if(e.key === "Backspace" && input.value === "" && index > 0){
            inputs[index-1].focus()
        }
    });

    input.addEventListener("paste", (e) => {
        e.preventDefault();
        const pasted = e.clipboardData.getData("text").replace(/\D/g, "").slice(0, 4);
        pasted.split("").forEach((char, i) => {
          if (inputs[i]) {
            inputs[i].value = char;
          }
        });
        if (inputs[pasted.length - 1]) {
          inputs[pasted.length - 1].focus();
        }
      });
});

// script to show password
const pass = document.getElementById('password');
const re_pass = document.getElementById('re_password');
const show_pass = document.getElementById('show_password');

show_pass.addEventListener('change', function(){
    pass.type = this.checked ? 'text' : 'password';
    re_pass.type = this.checked ? 'text' : 'password';
});

//SUMMARY
//summary text
window.addEventListener('DOMContentLoaded', ()=>{
    //taking season from url
    let querystring = window.location.search;
    let urlParam = new URLSearchParams(querystring);
    let season = urlParam.get('season');

    if(season == 'year'){
        document.getElementById('lol').hidden =false;
        document.getElementById('cs').hidden =false;
    }
    
    document.getElementById('text').innerHTML = "Check your " + season + " summary";
})

//selecting sport
document.getElementById('sport').addEventListener("change", function(){
    //taking season from url
    let querystring = window.location.search;
    let urlParam = new URLSearchParams(querystring);
    let season = urlParam.get('season');

    document.getElementById('text').style.visibility = 'hidden';

    const selected = this.value; //take selected value

    fetch('src/php/summary.php', {
        method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `season=${encodeURIComponent(season)}&sport=${encodeURIComponent(selected)}`
    })
    .then(response=>response.json())
    .then(data=>{
        if(data.home && data.away){
            document.getElementById('data').innerHTML = data.summary + data.home + data.away + data.leagues + data.teams;
        }else{
            document.getElementById('data').innerHTML = data.summary + data.leagues + data.teams;
        }
    })
})
