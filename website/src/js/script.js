// toggle menu script
const toggleMenuEl = document.getElementById('js-toggle-menu');
const toggleableMenuEl = document.getElementById('js-toggleable-menu');

toggleMenuEl?.addEventListener('click', function(){
    toggleableMenuEl?.classList.toggle('active');
})

const breakpoint = window.matchMedia('(min-width: 768px)');
breakpoint.addEventListener('change', function(){
    toggleableMenuEl?.classList.remove('active');
})

// script to show password
const pass = document.getElementById('password');
const re_pass = document.getElementById('re_password');
const show_pass = document.getElementById('show_password');

show_pass?.addEventListener('checked', function(){
    pass?.classList.value('show')
})