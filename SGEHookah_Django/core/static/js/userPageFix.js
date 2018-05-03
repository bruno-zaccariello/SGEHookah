function userPageFix() {
	var oamExtra = document.getElementById("oam_extra");
	var oamWrapper = document.getElementById("oam_wrapper");
	var searchWrapper = document.getElementById("search_wrapper");
	if(oamExtra) {
		oamWrapper.style.display = "none";
		searchWrapper.style.display = "none";
		oamExtra.innerHTML = '<a href="/iframe/home" target="main_frame" class="a_um_goback"><button onclick="userPageOff()" class="bt_um_goback">Retornar ao Sistema</button></a>';
		document.getElementById("menu_topping").style.borderBottom = "1px solid white";
		oamExtra.style.padding = "5px 0";
	}
}

function userPageOff() {
	var oamExtra = document.getElementById("oam_extra");
	var oamWrapper = document.getElementById("oam_wrapper");
	var searchWrapper = document.getElementById("search_wrapper");
	oamWrapper.style.display = "grid";
	searchWrapper.style.display = "flex";
	oamExtra.innerHTML = "";
	document.getElementById("menu_topping").style.borderBottom = "none";
}

function userPageFix2() {
	var loader = document.getElementById("main_frame").contentWindow.document.getElementById("user_main_body")
	if(loader) {
		userPageFix();
	}
	else {
		userPageOff()
	}
}