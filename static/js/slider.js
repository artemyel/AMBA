$(document).on('ready', function() {

  $(".regular").slick({
    dots: true,
    infinite: true,
    slidesToShow: 4,
    slidesToScroll: 4
  });
  $('.fade-slick').slick({
    dots: true,
    infinite: true,
    speed: 500,
    fade: true,
    adaptiveHeight: true,
    cssEase: 'linear',
    autoplay: true,
    autoplaySpeed: 3000,
  })
});
