function userPageFix() {
	var oamWrapper = document.getElementById("oam_wrapper"); 
	var searchWrapper = document.getElementById("search_wrapper");
	if(searchWrapper) {
        $('#main_frame').addClass('frame_height');
		oamWrapper.style.display = "none";
		$('#search_wrapper').addClass("hidden");
	}
}

function userPageOff() {
	var oamWrapper = document.getElementById("oam_wrapper");
	var oamExtra = document.getElementById("oam_extra");
	oamWrapper.style.display = "grid";
	$('#search_wrapper').removeClass("hidden");
    $('#main_frame').removeClass('frame_height');
}

function userPageFix2() {
	var loader = document.getElementById("main_frame").contentWindow.document.getElementById("user_main_body");
	var iFrame = document.getElementById("main_frame");
	if(loader) {
		userPageFix();
	}
	else {
		userPageOff();
	}
}