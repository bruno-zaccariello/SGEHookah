import datetime
import requests

from django.shortcuts import render, redirect
from django.http import request, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.db import transaction
from core.forms import *
from core.funcoes import *

import core.models as models

# fornecedor

@login_required(login_url="/admin")
def cadastrar_fornecedor(request):
    success = request.GET.get('success', False)
    if request.POST:
        fornecedorForm = FornecedorForm(request.POST)
        enderecoForm = EnderecoForm(request.POST)
        telefoneForm = TelefoneForm(request.POST)
        if fornecedorForm.is_valid() and enderecoForm.is_valid() and telefoneForm.is_valid():
            # Caso aja erro o atomic() irá desfazer as alteração feitas durante o código.
            with transaction.atomic() :
                # Altera o tipo de pessoa no formulario e salva
                fornecedorForm = fornecedorForm.save(commit=False)
                fornecedorForm.fornecedor = True
                fornecedorForm.save()
                pessoa = models.Pessoa.objects.get(pkid_pessoa=fornecedorForm.pk)

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
        fornecedorForm = FornecedorForm()
        enderecoForm = EnderecoForm()
        telefoneForm = TelefoneForm()
    context = {
            "fornecedorForm":fornecedorForm,
            "enderecoForm":enderecoForm,
            "telefoneForm":telefoneForm,
            "success":success
    }
    return render(request, "iframe/fornecedores/cadastrar_fornecedor.html", context)

@login_required(login_url="/admin")
def lista_fornecedores(request):
    # Pega informações da URL
    codigo = request.GET.get('search_cod_fornec', '')
    nome = request.GET.get('search_name_fornec', '')
    deletado = request.GET.get('deleted', False)
    page = int(request.GET.get('page', 1))

    # Filtra lista de clientes e gera páginas
    lista_fornecedores = filtra_pessoas(codigo, nome).filter(
        fornecedor=True
    )
    # função em funcoes.py
    paginas = Paginator(lista_fornecedores, 10)
    fornecedores = paginas.get_page(page)
    url = arruma_url_page(request) # função em funcoes.py

    context = {
        "fornecedores":fornecedores,
        "pagina":fornecedores,
        "deletado":deletado,
        "url":url
    }
    return render(request, "iframe/fornecedores/lista_fornecedores.html", context)

@login_required(login_url="/admin")
def deletar_fornecedor(request, id_fornecedor):
    fornecedor = models.Pessoa.objects.get(pkid_pessoa=id_fornecedor)
    fornecedor.hide = True
    fornecedor.save()
    return HttpResponseRedirect("/iframe/fornecedores/lista?deleted=True")