function ToggleMenu() {
	var menu = document.getElementById("oam_wrapper");
	var iFrame = document.getElementById("main_frame");
	if (menu.style.display == "none"){
		$('#oam_wrapper').slideToggle("fast", "linear");
		iFrame.style.height = "80%";
	} else if(menu.style.display == "grid") {
		$('#oam_wrapper').slideToggle("fast", "linear");
		iFrame.style.height = "100%";
	}
}
