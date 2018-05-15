function jasDisplayOn() {
	var jas = document.getElementById("janela_AlterarSenha");
	if(jas) {
		jas.style.display = "block"
	}
}

function jasDisplayOff() {
	var jas = window.parent.document.getElementById("janela_AlterarSenha");
	var erros = document.getElementById("errosFormSenha");
	if(jas) {
		jas.style.display = "none"
	}
	if(erros) {
		erros.outerHTML = ""
	}
}

function ShowErrosAs() {
	var erros = document.getElementById("errosFormSenha");
	if(erros) {
		jasDisplayOn();
	}
}

function alertSucessOff() {
	var alerta = document.getElementById("alerta");
	if(alerta) {
		alerta.style.display = "none"
		location.reload()
	}
}

function jas_alertSucessOn() {
	var alerta = window.parent.document.getElementById("alerta");
	if(alerta) {
		alerta.innerHTML = '<div class="jas_bg"></div><div class="alerta_wrapper" id=""><div class="trackSuccess"> Senha Alterada com Sucesso </div><div class="jas_bt_div"><button onclick="javascript:alertSucessOff()" class="btMain btConfirmar">Continuar</button></div></div>'
		alerta.style.display = "block"
	}
}

function jai_alertSucessOn() {
	var alerta = window.parent.document.getElementById("alerta");
	if(alerta) {
		alerta.innerHTML = '<div class="jas_bg"></div><div class="alerta_wrapper" id=""><div class="trackSuccess"> Informações Alteradas com Sucesso </div><div class="jas_bt_div"><button onclick="javascript:alertSucessOff()" class="btMain btConfirmar">Continuar</button></div></div>'
		alerta.style.display = "block"
	}
}

function jaiDisplayOn() {
	var jai = document.getElementById("janela_AlterarInfo");
	if(jai) {
		jai.style.display = "block"
	}
}

function jaiDisplayOff() {
	var jai = window.parent.document.getElementById("janela_AlterarInfo");
	if(jai) {
		jai.style.display = "none"
	}
}

function ShowErrosAi() {
	var erros = document.getElementById("errosFormUserInfo");
	if(erros) {
		jaiDisplayOn();
	}
}