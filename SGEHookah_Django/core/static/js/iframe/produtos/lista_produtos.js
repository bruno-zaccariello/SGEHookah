function confirmaJanelaOn(id) {
	var telaConfirma = document.getElementById("overlay");
	var bt_confirma = document.getElementById("bt_confirma");
	if(telaConfirma) {
		telaConfirma.style.display = "block";
		bt_confirma.href = "/iframe/produtos/deletar/" + id;
	}
}

function confirmaJanelaOff() {
	var telaConfirma = document.getElementById("overlay");
	var bt_confirma = document.getElementById("bt_confirma");
	if(telaConfirma) {
		telaConfirma.style.display = "none";
		bt_confirma.href = "";
	}
}