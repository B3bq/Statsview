// script to show password
const pass = document.getElementById('password');
const re_pass = document.getElementById('re_password');
const show_pass = document.getElementById('show_password');

show_pass.addEventListener('change', function(){
    pass.type = this.checked ? 'text' : 'password';
    re_pass.type = this.checked ? 'text' : 'password';
});