console.log("ola");

// bar, navbar, head

const head = document.querySelector('.head');
var navbar = document.querySelector('.navbar');
var bar = document.querySelector('.bar');
var xbar = document.querySelector('.Xbar');

bar.addEventListener('click', ()=>{
    navbar.style.display = 'flex';
    bar.style.display = 'none';
    xbar.style.display = 'flex';
});

xbar.addEventListener('click', ()=>{
    navbar.style.display = 'none';
    bar.style.display = 'flex';
    xbar.style.display = 'none';
})