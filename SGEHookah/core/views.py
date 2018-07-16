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

__all__ = ["index", "home", "redirect_home", "iframe_home", "cadastrar_produto", "user_main", "calcula_frete", "change_pw_form", "update_user_form", "product_page", "lista_produtos", "deletar_produto", "lista_categorias", "deletar_categoria", "lista_unidades", "deletar_unidade", "cadastrar_cliente", "cadastro_rapido_cliente", "lista_clientes"]

# Create your views here.
	
def index(request):
	return render(request, "index.html")

#Home e Principais	
	
@login_required(login_url="/admin")
def home(request):
	return render(request, "base.html")	

@login_required(login_url="/admin")
def redirect_home(request):
	return redirect('/admin')

@login_required(login_url="/admin")
def iframe_home(request):
	return render(request, "iframe/home.html")	

# Página do usuário

@login_required(login_url="/admin")	
def	change_pw_form(request):
	success = request.GET.get('success', False)
	if request.method == 'POST':
		form_pw = PasswordChangeForm(request.user, request.POST)
		if form_pw.is_valid():
			user = form_pw.save()
			update_session_auth_hash(request, user)
			url = str(request.path_info) + str('?success=True')
			return HttpResponseRedirect(url)
	else: 
		form_pw = PasswordChangeForm(request.user)

	# Checa se existe algum erro para ativar no template
	form_errors = False
	for field in form_pw :
		if field.errors:
			form_errors = True

	context = {
		"form_pw":form_pw,
		"success":success,
		"form_errors":form_errors
		}
	return render(request, "usuario/forms/AlterarSenha.html", context)

@login_required(login_url="/admin")
def update_user_form(request):
	success = request.GET.get('success', False)
	if request.method == 'POST':
		form_userInfo = UpdateInfoForm(request.POST, instance=request.user)
		if form_userInfo.is_valid():
			user = form_userInfo.save()
			update_session_auth_hash(request, user)
			url = str(request.path_info) + str('?success=True')
			return HttpResponseRedirect(url)
	else: 
		form_userInfo = UpdateInfoForm(instance=request.user)
	
	# Checa se existe algum erro para ativar no template
	form_errors = False
	for field in form_userInfo :
		if field.errors:
			form_errors = True

	context = {
		"form_userInfo":form_userInfo,
		"form_errors":form_errors,
		"success":success
	}
	return render(request, "usuario/forms/AlterarInfo.html", context)
	
@login_required(login_url="/admin")
def user_main(request):
	usuario = request.user
	context = {
		"user_usuario":usuario.get_username(),
		"user_name":usuario.get_full_name(),
		"user_email":usuario.email
	}
	return render(request, "usuario/user_main.html", context)
	
#Produto
	
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
	categorias = Categoriaproduto.objects.filter(hide=False)
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
			form.save()
			return HttpResponseRedirect(request.path_info)
	else :
		form = UnidademedidaForm()

	# Cria uma lista com as unidades visiveis (hide=False)
	unidades = Unidademedida.objects.filter(hide=False)
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
		

# Cliente

@login_required(login_url="/admin")
def cadastrar_cliente(request):
    success = request.GET.get('success', False)
    if request.POST:
        pessoaForm = PessoaForm(request.POST)
        enderecoForm = EnderecoForm(request.POST)
        telefoneForm = TelefoneForm(request.POST)
        if pessoaForm.is_valid() and enderecoForm.is_valid() and telefoneForm.is_valid():
            # Caso aja erro o atomic() irá desfazer as alteração feitas durante o código.
            with transaction.atomic() :
            	# Altera o tipo de pessoa no formulario e salva
                pessoaForm = pessoaForm.save(commit=False)
                pessoaForm.tipopessoa = 'cliente'
                pessoaForm.save()
                pessoa = Pessoa.objects.get(pkid_pessoa=pessoaForm.pk)

                # Atualiza o endereço com a pessoa recém criada e salva
                enderecoForm = enderecoForm.save(commit=False)
                enderecoForm.fkid_pessoa = pessoa
                enderecoForm.save()

                # Arruma o campo de telefone e salva
                telefoneForm = telefoneForm.save(commit=False)
                if telefoneForm.numero not in ('', None):
                    telefoneForm.fkid_pessoa = pessoa
                    numero = str(telefoneForm.numero)
                    telefoneForm.ddd = numero[1:3]
                    telefoneForm.numero = numero[4:]
                    telefoneForm.save()

                # Arruma a url para devolver que foi cadastrado com sucesso
                url = str(request.path_info) + str('?success=True')
                return HttpResponseRedirect(url)
    else:
        pessoaForm = PessoaForm()
        enderecoForm = EnderecoForm()
        telefoneForm = TelefoneForm()
    context = {
			"pessoaForm":pessoaForm,
            "enderecoForm":enderecoForm,
            "telefoneForm":telefoneForm,
			"success":success
	}
    return render(request, "iframe/clientes/cadastrar_cliente.html", context)

@login_required(login_url="/admin")
def cadastro_rapido_cliente(request):
	success = request.GET.get('success', False)
	if request.POST:
		pessoaForm = PessoaRapidoForm(request.POST)
		if pessoaForm.is_valid():
			pessoaForm = pessoaForm.save(commit=False)
			# Arruma o campo de e-mail para não ter conflito
			if pessoaForm.email == '':
				pessoaForm.email = None

			# Arruma o campo de cpf para não ter conflito
			if pessoaForm.cpf_cnpj == '':
				pessoaForm.cpf_cnpj = None

			pessoaForm.tipopessoa = 'cliente'
			pessoaForm.save()
		url = str(request.path_info) + '?success=True'
		return HttpResponseRedirect(url)
	else:
		pessoaForm = PessoaRapidoForm()
	context = {
	"pessoaForm":pessoaForm,
	"success":success,
	}
	return render(request, "iframe/clientes/cadastro_rapido_cliente.html", context)

@login_required(login_url="/admin")
def lista_clientes(request):
	# Pega informações da URL
	codigo = request.GET.get('search_cod_client', False)
	nome = request.GET.get('search_name_client', False)
	deletado = request.GET.get('deleted', False)
	page = int(request.GET.get('page', 1))

	# Filtra lista de clientes e gera páginas
	lista_clientes = filtra_clientes(codigo, nome) # função em funcoes.py
	paginas = Paginator(lista_clientes, 10)
	clientes = paginas.get_page(page)
	url = arruma_url_page(request) # função em funcoes.py
	
	context = {
		"clientes":clientes,
		"pagina":clientes,
		"deletado":deletado,
		"url":url
	}
	return render(request, "iframe/clientes/lista_clientes.html", context)

# Frete		
	
@login_required(login_url="/admin")
def calcula_frete(request):
	retorno = {"Valor":"0,00", "PrazoEntrega":0, "MsgErro":"None"}
	if request.POST:
		form = FreteForm(request.POST)
		if form.is_valid():
			# Arruma os campos de altura, comprimento e largura para não dar erro.
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