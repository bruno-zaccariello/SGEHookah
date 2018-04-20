function userPageFix() {
	var oamExtra = document.getElementById("oam_extra");
	var oamWrapper = document.getElementById("oam_wrapper");
	var searchWrapper = document.getElementById("search_wrapper");
	if(oamExtra) {
		oamWrapper.style.display = "none";
		searchWrapper.style.display = "none";
		oamExtra.innerHTML = '<a href="/admin/home"><button class="bt_um_goback">Retornar ao Sistema</button></a>';
		document.getElementById("menu_topping").style.borderBottom = "1px solid white";
		oamExtra.style.padding = "5px 0";
	}
}