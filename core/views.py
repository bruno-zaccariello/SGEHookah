from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from core.forms import Teste, FreteForm
import datetime
import requests
from xml.etree import ElementTree

'''
#Modelo

@login_required(login_url="/Login")
@user_passes_test(checa_professor)
def page_cadastro_disciplina(request):
    if request.POST:
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            print("DISCIPLINA CADASTRADA")
    else:
        form = DisciplinaForm()
    context = {
        "form":form
    }
    return render(request,"CadastrarDisciplina.html",context)

'''

__all__ = ["index", "home", "redirect_home", "iframe_home", "cadastrar_produto", "user_main", "calcula_frete"]

# Create your views here.
def calculo(
    nCdServico = "4014",
    sCepOrigem = "02415002",
    sCepDestino = "06436120",
    nVlPeso = "0.5",
    nCdFormato = 1,
    nVlComprimento = 20,
    nVlAltura = 20,
    nVlLargura = 20,
    nVlDiametro = "30",
    sCdMaoPropria = "N",
    nVlValorDeclarado = 0,
    sCdAvisoRecebimento = "N"):
    url = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPrecoPrazo?nCdEmpresa=&sDsSenha=&nCdServico={}&sCepOrigem={}&sCepDestino={}&nVlPeso={}&nCdFormato={}&nVlComprimento={}&nVlAltura={}&nVlLargura={}&nVlDiametro={}&sCdMaoPropria={}&nVlValorDeclarado={}&sCdAvisoRecebimento={}".format(nCdServico, sCepOrigem, sCepDestino, nVlPeso, nCdFormato, nVlComprimento, nVlAltura, nVlLargura, nVlDiametro, sCdMaoPropria, nVlValorDeclarado, sCdAvisoRecebimento)
    retorno = requests.get(url)
    tree = ElementTree.fromstring(retorno.content)
    dici = {}
    for child in tree.iter('*'):
        tag = child.tag.split('}')[1]
        dici[tag] = str(child.text)
    return dici
	
def index(request):
	return render(request, "index.html")
	
def user_main(request):
	return render(request, "usuario/user_main.html")
	
@login_required(login_url="/admin")
def home(request):
	return render(request, "base.html")
	
def redirect_home(request):
	return redirect('/admin')
	
def iframe_home(request):
	return render(request, "iframe/home.html")
	
def cadastrar_produto(request):
	if request.POST:
		form = Teste(request.POST)
		if form.is_valid():
			form.save()
			print("DISCIPLINA CADASTRADA")
	else:
		form = Teste()
	context = {
			"form":form
	}
	return render(request, "iframe/produtos/cadastrar_produto.html", context)

def calcula_frete(request):
	retorno = 0
	if request.POST:
		form = FreteForm(request.POST)
		if form.is_valid():
			retorno = calculo(
				form.cleaned_data['nCdServico'],
				form.cleaned_data['sCepOrigem'],
				form.cleaned_data['sCepDestino'],
				form.cleaned_data['nVlPeso'],
				form.cleaned_data['nCdFormato'],
				form.cleaned_data['nVlComprimento'],
				form.cleaned_data['nVlAltura'],
				form.cleaned_data['nVlLargura'],
				form.cleaned_data['nVlDiametro']
				)
	else:
		form = FreteForm()
	context = {"form":form, "resposta_frete":retorno}
	return render(request, "iframe/calcula_frete.html", context)