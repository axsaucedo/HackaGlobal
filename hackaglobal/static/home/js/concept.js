$(function(){
	var ww = $(window).width();
	if(ww > 640){$(".aboutimg img, .aboutimg .credit, #flow img, #flow h2, #gallery .galleryitem").css("opacity","0");};

	$(window).scroll(function(){
		var myHeader = document.getElementById('vi');

		var scrollTop = parseInt($(this).scrollTop()); //??????;
		var Hvi = $("#vi").height(); //???????????
		var OtopGnav = $("#top_gnav").offset(); //???????
		var ww = $(window).width();


		if ($(window).scrollTop() > 580) {
			$('#top_gnav').addClass('transition-header');
			$('.main-menu').delay(1000)
							.queue( function(next){
							$(this).css('position','fixed');
							next();
							});

            $('.globe-bracket').fadeIn('slow');
            $('#mc_embed_signup').addClass('transition-about');
            $('#account-buttons').addClass('no-list');

        }
        else if($(window).scrollTop() > 520) {
            $('#vi').css('margin-top', 520 - $(window).scrollTop());
            console.log("here")
            $('#mc_embed_signup').css('margin-top', '0px');
        }
        else {
            $('#mc_embed_signup').removeClass('transition-about');
            $('#account-buttons').removeClass('no-list');

            $('#vi').css('margin-top', 0);

            $('.globe-bracket').hide();

			$('#top_gnav').removeClass('transition-header');
			$('.main-menu').css('position','absolute');

		}

		// end else

		// main ????
		/*
		if (scrollTop < Hvi && ww > 640 ){
			$("#top_gnav").css({ position:"relative"});
			$("#top_gnav_dummy").addClass("disnon");
			$("#main").css("marginTop","" + scrollTop/2 + "px");
		} else if(scrollTop > Hvi && ww > 640 ){

			$("#top_gnav").css({
				'width': "100%",
				'max-width': "100%",
				'position' : "fixed",
				'top':"0",
			});

			$("#top_gnav_dummy").removeClass("disnon");
		} else if( ww <= 640 ){
			$("#main").css("marginTop","0px");
		}
		*/

		//vi_bg
		if(ww > 640){$("#vi_bg").css({ backgroundPosition:"0px -"+(scrollTop/10)+"px"});};

		// #about
		var Oabout = $("#about").offset();
		if (scrollTop > Oabout.top - 250 && ww > 640){$(".flyout01").animate({left: "0px", opacity:"1"})};
		if (scrollTop > Oabout.top - 50 && ww > 640){$(".flyout02").animate({right: "0px", opacity:"1"})};
		if (scrollTop > Oabout.top + 200 && ww > 640){$(".flyout03").animate({left: "0px", opacity:"1"})};
		if (scrollTop > Oabout.top + 400 && ww > 640){$(".flyout04, .flyout04+.credit").animate({right: "0px", opacity:"1"})};


		// .global
		$("ul.global_sub").hide();
		$("ul.global>li").hover(function(){
			$("ul:not(:animated)",this).slideDown()
		},
		function(){
			$("ul",this).slideUp();
		})
	});

	$('.hacka-scroll').click(function(){
		var speed = 800;
		var href= $(this).attr("href");
		var target = $(href == "#" || href == "" ? 'html' : href);
		var position = target.offset().top;
		$("html, body").animate({scrollTop:position}, speed, "swing");
		return false;
	});
});