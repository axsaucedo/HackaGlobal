$(function(){
	//ページトップ
    $("a.pagetop").click(function(){
    	$('html,body').animate({ scrollTop: 0 }, 'slow','swing');
    	return false;
    });
	 
	//グローバル切替(PC)
    $("ul.global_sub").hide();
    $("ul.global>li").hover(function(){
    	$("ul:not(:animated)",this).slideDown()
    },
    function(){
        $("ul",this).slideUp();
    })
	
    // サイドメニュー
    $("#simple-menu").sidr({
        side: 'right'
    });

    // サイドメニュー言語切替
    var isMenuLangOpen = false;
    $(".manu_lang_list").hide();
    $("a.menu_lang_changer").click(function(e){
        e.preventDefault();
        if(isMenuLangOpen) {
            $(".menu_lang_changer").removeClass("open");
            isMenuLangOpen = false;
        }else{
            $(".menu_lang_changer").addClass("open");
            isMenuLangOpen = true;
        }
        $('.manu_lang_list').slideToggle();
    });

    setCountryUrl();

    function setCountryUrl(){
        var currentUrl = window.location.pathname;
        var coutryCode = currentUrl.substr(0, 4);

        var jaUrl = currentUrl.replace(coutryCode, "/ja/");
        var enUrl = currentUrl.replace(coutryCode, "/en/");
        var frUrl = currentUrl.replace(coutryCode, "/fr/");
        var deUrl = currentUrl.replace(coutryCode, "/de/");
        var ukUrl = currentUrl.replace(coutryCode, "/uk/");
        $(".country_jp").attr("href", jaUrl);
        $(".country_us").attr("href", enUrl);
        $(".country_fr").attr("href", frUrl);
        $(".country_de").attr("href", deUrl);
        $(".country_uk").attr("href", ukUrl);
    }
});

function converter(M){
var str="", str_as="";
for(var i=0;i<M.length;i++){
str_as = M.charCodeAt(i);
str += String.fromCharCode(str_as + 1);
}
return str;
}
