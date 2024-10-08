document.addEventListener("DOMContentLoaded", function() {
    var hamburger = document.querySelector('.hamburger'); 
    var menu = document.querySelector('.main-menu ul'); 
    var submenuToggle = document.querySelector('.submenu-toggle'); 
    var submenu = document.querySelector('.submenu ul'); 
    hamburger.addEventListener('click', function() {
        menu.classList.toggle('open');
    });
});
