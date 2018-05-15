from django.shortcuts import render, redirect
from django.http import request, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from decimal import *
from core.forms import *
from core.models import *
import datetime
import requests
from core.funcoes import *
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

__all__ = ["index", "home", "redirect_home", "iframe_home", "cadastrar_produto", "user_main", "calcula_frete", "altera_senha_form", 
"atualiza_user_form", "pagina_produto", "lista_produtos", "deletar_produto", "lista_categorias", "deletar_categoria"]

# Create your views here.
	
def index(request):
	return render(request, "index.html")

#Home e Principais	
	
@login_required(login_url="/admin")
def home(request):
	return render(request, "base.html")	

def redirect_home(request):
	return redirect('/admin')

def iframe_home(request):
	return render(request, "iframe/home.html")	

# Página do usuário
	
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
	context = {
		"form_senha":form_senha,
		"senhaAlterada":senhaAlterada,
		"errosFormSenha":erros
		}
	return render(request, "usuario/forms/AlterarSenha.html", context)

def atualiza_user_form(request):
	infoAlterada = False
	if request.method == 'POST':
		form_userInfo = UpdateInfoForm(request.POST, instance=request.user)
		if form_userInfo.is_valid():
			user = form_userInfo.save()
			update_session_auth_hash(request, user)
			infoAlterada = True
		else:
			messages.error(request, 'Error')
	else: 
		form_userInfo = UpdateInfoForm(instance=request.user)
	erros = []
	for field in form_userInfo :
		if field.errors:
			erros.append(field.errors)
	if len(erros) == 0 :
		erros = 'none'
	context = {
		"form_userInfo":form_userInfo,
		"errosFormUserInfo":erros,
		"infoAlterada":infoAlterada
	}
	return render(request, "usuario/forms/AlterarInfo.html", context)
	
def user_main(request):
	usuario = request.user
	context = {
		"user_usuario":usuario.get_username(),
		"user_nome":usuario.get_full_name(),
		"user_email":usuario.email
	}
	return render(request, "usuario/user_main.html", context)
	
#Produto
	
def cadastrar_produto(request):
	success = request.GET.get('success', False)
	if request.POST:
		form = ProdutoForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit=False)
			if form.fotoproduto == '' or form.fotoproduto == None :
				form.fotoproduto = 'default_product.png'
			form.totalestoque = 0
			form.hide = 0
			form.save()
			url = str(request.path_info) + str('?success=True')
			return HttpResponseRedirect(url)
	else:
		form = ProdutoForm()
	context = {
			"form":form,
			"success":success
	}
	return render(request, "iframe/produtos/cadastrar_produto.html", context)

def pagina_produto(request, id_produto):
	try :
		produto = Produto.objects.get(pkid_produto=id_produto)
	except:
		return HttpResponseRedirect('/admin/home')
	context = {
		"produto":produto
	}
	return render(request, "iframe/produtos/pagina_produto.html", context)		
			
def lista_produtos(request):
	codigo = request.GET.get('search_cod_produto', False)
	pChave = request.GET.get('search_keyword_prod', False)
	deletado = request.GET.get('deleted', False)
	page = int(request.GET.get('page', 1))
	lista_produtos = filtra_produtos(codigo, pChave) #função em funcoes.py
	paginas = Paginator(lista_produtos, 10)
	produtos = paginas.get_page(page)
	url = arruma_url_page(request) #função em funcoes.py
	context = {
		"produtos":produtos,
		"pagina":produtos,
		"deletado":deletado,
		"url":url
	}
	return render(request, "iframe/produtos/lista_produtos.html", context)
	
def deletar_produto(request, id_produto):
		try :
			produto = Produto.objects.get(pkid_produto=id_produto)
			produto.hide = True
			produto.dt_alteracao = datetime.datetime.now()
			produto.save()
		except :
			return HttpResponseRedirect('/iframe/produtos/lista?deleted=False'), 400
		return HttpResponseRedirect('/iframe/produtos/lista?deleted=True')

def lista_categorias(request):
	num_p = int(request.GET.get('page', 1))
	if request.POST:
		form = CategoriaprodutoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(request.path_info)
	else :
		form = CategoriaprodutoForm()
	categorias = Categoriaproduto.objects.filter(hide=False)
	pagina = paginar(categorias) #função em funcoes.py
	n_paginas = pagina.keys()
	if len(pagina[1]) == 0 :
		n_paginas = []
	url = arruma_url_page(request) #função em funcoes.py
	context = {
		"categorias":categorias,
		"form":form,
		"pagina":pagina[num_p],
		"n_paginas":n_paginas,
		"url":url
	}
	return render(request, "iframe/produtos/categoria/lista_categorias.html", context)
	
def deletar_categoria(request, id_categoria):
	categoria = Categoriaproduto.objects.get(pkid_categoria=id_categoria)
	categoria.hide = True
	categoria.save()
	return HttpResponseRedirect('/iframe/produtos/categorias')
		
#Frete		
	
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
			try :
				retorno = calculoFrete(
					form.cleaned_data['nCdServico'],
					form.cleaned_data['sCepOrigem'],
					form.cleaned_data['sCepDestino'],
					form.cleaned_data['nVlPeso'],
					form.cleaned_data['nCdFormato'],
					form.cleaned_data['nVlComprimento'],
					form.cleaned_data['nVlAltura'],
					form.cleaned_data['nVlLargura']
					)
			except :
				print("Você está sem internet")
	else:
		form = FreteForm()
	context = {
	"form":form, 
	"Valor":retorno.get('Valor'), 
	"PrazoEntrega":retorno.get('PrazoEntrega'), 
	"MsgErro":retorno.get('MsgErro')
	}
	return render(request, "iframe/vendas/calcula_frete.html", context)