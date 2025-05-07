const toggleMenuEl = document.getElementById('js-toggle-menu');
const toggleableMenuEl = document.getElementById('js-toggleable-menu');

toggleMenuEl?.addEventListener('click', function(){
    toggleableMenuEl?.classList.toggle('active');
})

const breakpoint = window.matchMedia('(min-width: 768px)');
breakpoint.addEventListener('change', function(){
    toggleableMenuEl?.classList.remove('active');
})