function jasDisplayOn() {
	var jas = document.getElementById("janela_AlterarSenha");
	if(jas) {
		jas.style.display = "block"
	}
}

function jasDisplayOff() {
	var jas = document.getElementById("janela_AlterarSenha");
	if(jas) {
		jas.style.display = "none"
	}
}

function ShowErros() {
	var erros = document.getElementById("errosFormSenha");
	if(erros) {
		jasDisplayOn();
		fixForm();
	}
}

function alertSucessOff() {
	var alerta = document.getElementById("alerta_wrapper");
	if(alerta) {
		alerta.style.display = "none"
	}
}

function fixForm() {
	var wp_form = document.getElementById("wp_AlterarSenhaForm");
	if(wp_form) {
		wp_form.style.height = '45%'
	}
}