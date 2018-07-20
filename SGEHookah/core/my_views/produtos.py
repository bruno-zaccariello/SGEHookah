import datetime
import requests

from django.shortcuts import render, redirect
from django.http import request, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.db import transaction
from django.forms import formset_factory, modelformset_factory, inlineformset_factory
from xml.etree import ElementTree
from decimal import *
from core.forms import *
from core.models import *
from core.funcoes import *

# Produto
	
@login_required(login_url="/admin")
def cadastrar_produto(request):
	success = request.GET.get('success', False)
	if request.POST:
		form = CadProdutoForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit=False)

			# Define uma imagem padrão caso nenhuma tenha sido escolhida
			if form.fotoproduto == '' or form.fotoproduto == None :
				form.fotoproduto = 'default_product.png'

			form.save()
			url = str(request.path_info) + str('?success=True')
			return HttpResponseRedirect(url)
	else:
		form = CadProdutoForm()
	context = {
			"form":form,
			"success":success
	}
	return render(request, "iframe/produtos/cadastrar_produto.html", context)

@login_required(login_url="/admin")
def product_page(request, id_produto):
	# Tenta buscar o produto requerido
	# Caso falhe retorna à página inicial
	try :
		produto = Produto.objects.get(pkid_produto=id_produto)
	except:
		return HttpResponseRedirect('/admin/home')

	if request.POST :
		form = ProdutoForm(request.POST, request.FILES, instance=produto)

		# Checa se o formulário é valido e se foi alterado
		if form.is_valid() and form.has_changed() :
			form.save()
			return HttpResponseRedirect(request.path_info)
	else :
		form = ProdutoForm(instance=produto)

	# For Custom Form fields
	form_page = []
	for field in form :
		form_page.append(field)

	context = {
		"produto":produto,
		"form":form,
		"form_page":form_page[:-2]
	}
	return render(request, "iframe/produtos/pagina_produto.html", context)		
			
@login_required(login_url="/admin")
def lista_produtos(request):
	# Filtros e adicionais na URL
	codigo = request.GET.get('search_cod_produto', False)
	pChave = request.GET.get('search_keyword_prod', False)
	deletado = request.GET.get('deleted', False)
	page = int(request.GET.get('page', 1))

	# Funções para filtrar e gerar páginas
	lista_produtos = filtra_produtos(codigo, pChave) # Função em funcoes.py
	paginas = Paginator(lista_produtos, 10)
	produtos = paginas.get_page(page)

	url = arruma_url_page(request) # Função em funcoes.py
	context = {
		"pagina":produtos,
		"deletado":deletado,
		"url":url
	}
	return render(request, "iframe/produtos/lista_produtos.html", context)
	
@login_required(login_url="/admin")
def deletar_produto(request, id_produto):
		try :
			produto = Produto.objects.get(pkid_produto=id_produto)
			produto.hide = True
			produto.save()
		except :
			return HttpResponseRedirect('/iframe/produtos/lista?deleted=False'), 400
		return HttpResponseRedirect('/iframe/produtos/lista?deleted=True'), 500

@login_required(login_url="/admin")
def lista_categorias(request):
	# Pega o numero da pagina e se obteve sucesso deletando da URL
	num_p = int(request.GET.get('page', 1))
	success = request.GET.get('success', False)
	page = int(request.GET.get('page', 1))

	if request.POST:
		form = CategoriaprodutoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(request.path_info)
	else :
		form = CategoriaprodutoForm()

	# Funções para gerar páginas
	categorias = Categoriaproduto.objects.filter(hide=False).order_by('pkid_categoria')
	paginas = Paginator(categorias, 10)
	categorias = paginas.get_page(page)
	url = arruma_url_page(request) #função em funcoes.py

	context = {
		"form":form,
		"pagina":categorias,
		"url":url,
		"success":success
	}
	return render(request, "iframe/produtos/categoria/lista_categorias.html", context)
	
@login_required(login_url="/admin")
def deletar_categoria(request, id_categoria):
	categoria = Categoriaproduto.objects.get(pkid_categoria=id_categoria)
	categoria.hide = True
	categoria.save()
	return HttpResponseRedirect('/iframe/produtos/categorias?success=True')
		
@login_required(login_url="/admin")
def lista_unidades(request):
	# Pega o numero da pagina e se obteve sucesso deletando da URL
	num_p = int(request.GET.get('page', 1))
	success = request.GET.get('success', False)
	page = int(request.GET.get('page', 1))

	if request.POST:
		form = UnidademedidaForm(request.POST)
		if form.is_valid():
			try:
				exists = Unidademedida.objects.get(unidademedida=form.cleaned_data['unidademedida'])
				exists.hide = False
				exists.save()
			except:
				form.save()
			return HttpResponseRedirect(request.path_info)
	else :
		form = UnidademedidaForm()

	# Cria uma lista com as unidades visiveis (hide=False)
	unidades = Unidademedida.objects.filter(hide=False).order_by('pkid_unidademedida')
	paginas = Paginator(unidades, 10)
	unidades = paginas.get_page(page)
	url = arruma_url_page(request)

	context = {
		"form":form,
		"pagina":unidades,
		"url":url,
		"success":success
	}
	return render(request, "iframe/produtos/unidade/lista_unidade.html", context)
		
@login_required(login_url="/admin")
def deletar_unidade(request, id_unidade):
	unidade = Unidademedida.objects.get(pkid_unidademedida=id_unidade)
	unidade.hide = True
	unidade.save()
	return HttpResponseRedirect('/iframe/produtos/unidades?success=True')