function userPageFix() {
	var oamWrapper = document.getElementById("oam_wrapper"); 
	var searchWrapper = document.getElementById("search_wrapper");
	if(searchWrapper) {
		oamWrapper.style.display = "none";
		searchWrapper.style.display = "none";
		oamWrapper.style.borderBottom = "1px solid white"
		document.getElementById("menu_topping").style.borderBottom = "1px solid white";
	}
}

function userPageOff() {
	var oamWrapper = document.getElementById("oam_wrapper");
	var oamExtra = document.getElementById("oam_extra");
	var searchWrapper = document.getElementById("search_wrapper");
	oamWrapper.style.display = "grid";
	oamWrapper.style.borderBottom = "1px solid black"
	searchWrapper.style.display = "flex";
	document.getElementById("menu_topping").style.borderBottom = "none";
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