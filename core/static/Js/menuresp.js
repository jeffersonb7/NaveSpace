const btnMobile = document.getElementById('botaomobile');

function toggleMenu(event){
    if(event.type === 'touchstart') event.preventDefault();
    const nav = document.getElementById('nav');
    nav.classList.toggle('active');
}

btnMobile.addEventListener('click', toggleMenu);
//para deixar a abertura da nav mais rápida
btnMobile.addEventListener('touchstart', toggleMenu);



btnMobile.addEventListener('click', toggleMenu);
const btnhome = document.getElementById('construcao');

function togglePopup(){
    alert('Página ainda em desenvolvimento');
}