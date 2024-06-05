const swiper = new Swiper('.blog-slider', {
    spaceBetween: 30,
    effect: 'fade',  //slide
    loop: true,  //eslai false ma rakda herneyy ok
    mousewheel: {
      invert: false, 
    },
    pagination: {
      el: '.blog-slider__pagination',
      clickable: true,
    }
  });
  
