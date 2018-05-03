from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from core.forms import *
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
	
def index(request):
	return render(request, "index.html")

def	altera_senha_form(request):
	senhaAlterada = False
	if request.method == 'POST':
		form_senha = PasswordChangeForm(request.user, request.POST)
		if form_senha.is_valid():
			user = form_senha.save()
			update_session_auth_hash(request, user)
			senhaAlterada = True
		else:
			messages.error(request, 'Error')
	else: 
		form_senha = PasswordChangeForm(request.user)
	erros = []
	for field in form_senha :
		if field.errors:
			erros.append(field.errors)
	if len(erros) == 0 :
		erros = 'none'
	print(erros)
	return form_senha, senhaAlterada, erros

def atualiza_user_form(request):
	if request.method == 'POST':
		form_userInfo = UpdateInfoForm(request.POST, instance=request.user)
		if form_userInfo.is_valid():
			user = form_userInfo.save()
			update_session_auth_hash(request, user)
		else:
			messages.error(request, 'Error')
	else: 
		form_userInfo = UpdateInfoForm(instance=request.user)
	erros = []
	for field in form_senha :
		if field.errors:
			erros.append(field.errors)
	if len(erros) == 0 :
		erros = 'none'
	print(erros)
	return form_userInfo, erros
	
def user_main(request):
	form_senha, senhaAlterada, errosFormSenha = altera_senha_form(request)
	form_userInfo = atualiza_user_form(request)
	usuario = request.user
	context = {
		"user_usuario":usuario.get_username(),
		"user_nome":usuario.get_full_name(),
		"user_email":usuario.email,
		"form_senha":form_senha,
		"senhaAlterada":senhaAlterada,
		"errosFormSenha":errosFormSenha,
		"form_userInfo":form_userInfo
	}
	return render(request, "usuario/user_main.html", context)
	
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

def calculo(
    nCdServico = "4014",
    sCepOrigem = "",
    sCepDestino = "",
    nVlPeso = "0.5",
    nCdFormato = 1,
    nVlComprimento = 16,
    nVlAltura = 2,
    nVlLargura = 11,
    nVlDiametro = "0",
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
	
def calcula_frete(request):
	retorno = {"Valor":"0,00", "PrazoEntrega":0, "MsgErro":"None"}
	if request.POST:
		form = FreteForm(request.POST)
		if form.is_valid():
			if form.cleaned_data['nVlAltura'] < 2 :
				form.cleaned_data['nVlAltura'] = 2
			if form.cleaned_data['nVlComprimento'] < 16 :
				form.cleaned_data['nVlComprimento'] = 16
			if form.cleaned_data['nVlLargura'] < 11 :
				form.cleaned_data['nVlLargura'] = 11
			retorno = calculo(
				form.cleaned_data['nCdServico'],
				form.cleaned_data['sCepOrigem'],
				form.cleaned_data['sCepDestino'],
				form.cleaned_data['nVlPeso'],
				form.cleaned_data['nCdFormato'],
				form.cleaned_data['nVlComprimento'],
				form.cleaned_data['nVlAltura'],
				form.cleaned_data['nVlLargura']
				)
	else:
		form = FreteForm()
	context = {
	"form":form, 
	"Valor":retorno.get('Valor'), 
	"PrazoEntrega":retorno.get('PrazoEntrega'), 
	"MsgErro":retorno.get('MsgErro')
	}
	return render(request, "iframe/vendas/calcula_frete.html", context)