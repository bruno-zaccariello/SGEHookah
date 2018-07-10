function getTitle() {
	var iframeTitle = document.getElementById("main_frame").contentWindow.document.getElementById("iframe_title");
	var baseTitle = document.getElementById("base_title");
	if(iframeTitle) {
		baseTitle.textContent = iframeTitle.textContent;
	}
}

function oamTitle() {
	var iframeTitle = document.getElementById("main_frame").contentWindow.document.getElementById("iframe_title");
	var oamTitle = document.getElementById("oam_extra");
	var oamExtraTitle = document.getElementById("oam_extra_title");
	if(oamTitle) {
		if(oamExtraTitle){
			oamExtraTitle.parentNode.removeChild(oamExtraTitle);
		}
		oamTitle.innerHTML += ("<div id='oam_extra_title' class='oam_extra_title hidden'>"+iframeTitle.textContent+"</div>");
	}
}