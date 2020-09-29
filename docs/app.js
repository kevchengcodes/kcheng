var main = function () {

jQuery("document").ready(function($){
	var nav=$('.nav-container');
	$(window).scroll(function(){
		if ($(this).scrollTop()>300){
			nav.addClass("f-nav");
		}
		else {nav.removeClass("f-nav");}
	});
});
	
      $('.icon-menu').click(function() {
    $('.menu').animate({
      left: '0px'
    }, 200);

    $('body').animate({
      left: '285px'
    }, 200);
  });
  $('.icon-close').click(function() {
  $('.menu').animate({
  left: '-285px'
  },200);
  $('body').animate({
  left: '0px'},200);
  })

  $('.article').click(function() {
        $('.article').removeClass('current');
        $('.description').hide();
        
        $(this).addClass('current');
        $(this).children('.description').toggle();
    })

    // $(document).keypress(function(event) {
    // if(event.which === 111){
    //     $('.current').children('.description').toggle();}
    // else if(event.which === 110){
    //     var currentArticle = $('.current');
    //     var nextArticle = currentArticle.next();
        
    //     currentArticle.removeClass('current');
    //     nextArticle.addClass('current');
    // }
    // })
};

$(document).ready(main);