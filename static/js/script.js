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

// O IntersectionObserver serve para observar intens na tela, diz quendo e que esses itens estao visiveis quando se faz o scrooll.
const myObserver = new IntersectionObserver((entries) =>{
    entries.forEach((entry)=>{
        console.log(entries)
        if(entry.isIntersecting){
            entry.target.classList.add('show');
        }
        else{
            entry.target.classList.remove('show');
        }
    })
});

var elements = document.querySelectorAll('.hidden');
elements.forEach((element) => myObserver.observe(element))


// Efeito do scroll 
const  meunlink = document.querySelectorAll('.menu a[href^="#"]');

function ScrollToSection(event){
    event.preventDefault();
    const distanceFromTheTop = getDistanceFromTheTop(event.target) - 90;
    console.log(event.target);
    smoothScrollTo(0,  distanceFromTheTop, 1500);
}

function getDistanceFromTheTop(element){
    const id = element.getAttribute("href");
    return document.querySelector(id).offsetTop;
}

meunlink.forEach((link) => {
    link.addEventListener('click', ScrollToSection);
});

function smoothScrollTo(endX, endY, duration){
    const startX = window.scrollX || window.pageXOffset;
    const startY = window.scrollY || window.pageYOffset;
    const distanceX = endX - startX;
    const distanceY = endY - startY;
    const startTime = new Date().getTime();

    duration = typeof duration !== "underfined" ? duration : 400;

    const easeInOutQuart = (time, from, distance, duration) =>{
        if((time /= duration / 2) < 1)
            return (distance / 2) * time * time * time * time + from;
        return (-distance / 2) * ((time -= 2) * time * time * time - 2) + from;
    };

    const timer = setInterval(() => {
        const time = new Date().getTime() - startTime;
        const newX = easeInOutQuart(time, startX, distanceX, duration);
        const newY = easeInOutQuart(time, startY, distanceY, duration);
        if (time >= duration){
            clearInterval(timer);
        }
        window.scroll(newX, newY);

    }, 1000 / 60 );
}
