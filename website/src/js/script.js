import {deleteCookie} from './functions.js';

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

//listening
window.addEventListener('DOMContentLoaded', ()=>{
    const userID = getCookie("user"); //user id
    const userName = getCookie("name"); //user name
    console.log(document.cookie);

    if(userID){
        document.getElementById('logout').innerHTML = "Log out";
        document.getElementById('logout').title = "Log out";
        document.getElementById('logout').onclick = ()=>{
            deleteCookie('user');
            deleteCookie('name');
            document.getElementById('logout').innerHTML = "Log in";
            document.getElementById('logout').title = "Log in";
        };
        document.getElementById('userName').innerHTML = `${userName}`;
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