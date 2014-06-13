$(document).ready(function() {
	var nav_path = window.location.pathname.substring(1,window.location.pathname.length);
	if(nav_path == ""){
		nav_path = "/";
	}

	$("ul.nav > li > a").each(function(e){ 
		if( $(this).attr("href") == nav_path ){
			$(this).parent().addClass("active");
		} else {
			$(this).parent().removeClass("active");
		} 
	});

	if( $('.carousel').length > 0) {
		$('.carousel').carousel();
	}
});