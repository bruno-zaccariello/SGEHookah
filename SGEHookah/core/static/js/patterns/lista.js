function confirmaJanelaOff() {
	var telaConfirma = document.getElementById("overlay");
	var bt_confirma = document.getElementById("bt_confirma");
	if(telaConfirma) {
		telaConfirma.style.display = "none";
		bt_confirma.href = "";
	}
}

function showOvCad() {
	var overlay = document.getElementById("ov_cad");
	var base = window.parent.document
	if(overlay) {
		overlay.style.display = "block"
		// $(base).find('.overlayBG').removeClass('hidden')
	}
}

function hideOvCad() {
	var overlay = document.getElementById("ov_cad");
	if(overlay) {
		overlay.style.display = "none"
	}
}