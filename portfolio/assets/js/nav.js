const navbar = document.getElementById('navbar');
const scrollBtn = document.getElementById('scrollBtn');
let prevScrollpos = window.pageYOffset;

window.onscroll = function() {
  const currentScrollPos = window.pageXOffset;
  if (prevScrollpos > currentScrollPos) {
    navbar.style.top = '0';
    scrollBtn.style.display = 'none';
  } else {
    navbar.style.top = '-100px'; // Adjust this value to hide the navbar completely
    scrollBtn.style.display = 'block';
  }
  prevScrollpos = currentScrollPos;
};

scrollBtn.addEventListener('click', function() {
  window.scrollTo({top: 0, behavior: 'smooth'});
});
