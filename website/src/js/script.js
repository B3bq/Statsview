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

// script to show password
const pass = document.getElementById('password');
const re_pass = document.getElementById('re_password');
const show_pass = document.getElementById('show_password');

show_pass.addEventListener('change', function(){
    pass.type = this.checked ? 'text' : 'password';
    re_pass.type = this.checked ? 'text' : 'password';
});