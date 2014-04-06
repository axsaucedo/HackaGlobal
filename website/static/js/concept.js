$(function(){
	var ww = $(window).width();
	if(ww > 640){$(".aboutimg img, .aboutimg .credit, #flow img, #flow h2, #gallery .galleryitem").css("opacity","0");};
	
	//ギャラリーのサイズ設定
	function galleryCap(){
		var Hgallery = $("#gallery .galleryitem img").height(); //ギャラリーmin640の高さ
		$(".galleryitem div").css({"height": + Hgallery +"px"});

		var galleryWidth = $("#gallery").innerWidth();
		var galleryListWidth = $("#gallery_list").innerWidth();
		var marginWidth = ((galleryWidth - galleryListWidth) / 2) - 50;

		$("#leftctrl").animate({top:(Hgallery/2), left:marginWidth}, 200);
		$("#rightctrl").animate({top:(Hgallery/2), right:marginWidth}, 200);
		
		var HgallerySp = $("#gallery_sp li img").height(); //ギャラリーmax640の高さ
		$("#gallery_sp li div").css({"height": + HgallerySp +"px"});
	}

	function setSpGallery(){
		var itemnum = $("#gallery_list_sp").children().length - 1;
		var displayitemnum = 5;
		
		if(itemnum > displayitemnum){
			for (var i = 0; i < itemnum; i++) {
				if(i < displayitemnum){
					$($("#gallery_list_sp").children()[i]).show();
				}else{
					$($("#gallery_list_sp").children()[i]).hide();
				}
			}

			$(".morebtn").show();

			$.data($("#gallery_more_btn")[0], "currentnum", displayitemnum);

			$("#gallery_more_btn").click(function(e){
				e.preventDefault();
				var num = jQuery.data(this, "currentnum");
				var displaynum = num + displayitemnum;
				for (var i = num; i < displaynum; i++) {
					$($("#gallery_list_sp").children()[i]).show();
				}

				if(displaynum >= (itemnum-1)){
					$(".morebtn").hide();
				}else{
					$.data(this, "currentnum", displaynum);
				}
			});
		}else{
			$(".morebtn").hide();
		}
	}
	
	//読み込み後の処理
	$(window).load(function() {
		galleryCap();

	    $(".video1").colorbox({iframe:true, innerWidth:640, innerHeight:360, opacity:1});
	    $(".video2").colorbox({iframe:true, innerWidth:640, innerHeight:360, opacity:1});

	    setSpGallery();
	});

	// Gallery Hover
	$("#gallery .galleryitem").hover(function(){
    	$(this).find("div").stop().fadeTo(400,1);
    },
    function(){
        $(this).find("div").stop().fadeTo(300,0);
    });
	
	//ウインドウ可変時の処理
	var timer = false;
	$(window).resize(function() {
		if (timer !== false) {
			clearTimeout(timer);
		}
		timer = setTimeout(function() {
			//処理
			
			galleryCap();
			var ww = $(window).width();
			if(ww <= 640){ 
				$("#main").css("marginTop","0px");
				$(".aboutimg img, .aboutimg .credit, #flow img, #flow h2").css("opacity","1");
			};
			
		}, 200);
	});
	
	//スクロール時の処理
	$(window).scroll(function(){		
		var myHeader = document.getElementById('vi');
		
		var scrollTop = parseInt($(this).scrollTop()); //スクロール量;
		var Hvi = $("#vi").height(); //メインビジュアルの高さ
		var OtopGnav = $("#top_gnav").offset(); //グロナビの位置
		var ww = $(window).width();
		
		if ($(window).scrollTop() > 500) {
			$('#top_gnav').addClass('transition-header');
			$('.main-menu').delay(1000)
							.queue( function(next){ 
							$(this).css('position','fixed'); 
							next(); 
							});
			$('.globe-bracket').fadeIn('slow');
		} else {
			$('.globe-bracket').hide();
			$('#top_gnav').removeClass('transition-header');
			$('.main-menu').css('position','absolute');
		}
		
		// end else
		
		// main 動作固定
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
	
	$('a[href^=#]').click(function(){
		var speed = 800;
		var href= $(this).attr("href");
		var target = $(href == "#" || href == "" ? 'html' : href);
		var position = target.offset().top;
		$("html, body").animate({scrollTop:position}, speed, "swing");
		return false;
	});
});