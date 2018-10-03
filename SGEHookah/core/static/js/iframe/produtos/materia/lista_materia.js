function confirmaJanelaOn(id) {
	var telaConfirma = document.getElementById("overlay");
	var bt_confirma = document.getElementById("bt_confirma");
	telaConfirma.style.display = "block";
	bt_confirma.href = ""
	bt_confirma.href = "/iframe/produtos/materia/deletar/" + id;
}