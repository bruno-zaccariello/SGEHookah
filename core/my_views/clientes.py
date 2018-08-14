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

@login_required(login_url="/admin")
def deletar_cliente(request, id_cliente):
	cliente = Pessoa.objects.get(pkid_pessoa=id_cliente)
	cliente.hide = True
	cliente.save()
	return HttpResponseRedirect("/iframe/clientes/lista?deleted=True")