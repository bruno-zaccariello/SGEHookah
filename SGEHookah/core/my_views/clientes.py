"""
    Módulo que contem as views de produção
"""

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import transaction

from core.funcoes import arruma_url_page, filtra_clientes
from core.models import *
from core.forms import *


@login_required(login_url="/admin")
def cadastrar_cliente(request):
    """ Página para cadastrar um novo cliente """

    success = request.GET.get('success', False)
    if request.POST:
        form_pessoa = PessoaForm(request.POST)
        form_endereco = EnderecoForm(request.POST)
        form_telefone = TelefoneForm(request.POST)
        with transaction.atomic():
            if form_pessoa.is_valid():
                pessoa = form_pessoa.save(commit=False)
                pessoa.tipopessoa = 'cliente'
                pessoa.save()

                if form_endereco.is_valid():
                    form_endereco = form_endereco.save(commit=False)
                    form_endereco.fkid_pessoa = pessoa
                    form_endereco.save()

                if form_telefone.is_valid():
                    telefone = form_telefone.save(commit=False)
                    numero = telefone.numero
                    telefone.numero = numero[4:].replace('-','')
                    telefone.ddd = numero[1:3]
                    telefone.fkid_pessoa = pessoa
                    telefone.save()

                    # Arruma a url para devolver que foi cadastrado com sucesso
                    url = str(request.path_info) + str('?success=True')
                    return HttpResponseRedirect(url)
    else:
        form_pessoa = PessoaForm()
        form_endereco = EnderecoForm()
        form_telefone = TelefoneForm()
    context = {
        "pessoaForm": form_pessoa,
        "enderecoForm": form_endereco,
        "telefoneForm": form_telefone,
        "success": success
    }
    return render(request, "iframe/clientes/cadastrar_cliente.html", context)


@login_required(login_url="/admin")
def cadastro_rapido_cliente(request):
    """ Página para cadastrar rápido um cliente """

    success = request.GET.get('success', False)
    if request.POST:
        form_pessoa = PessoaRapidoForm(request.POST)
        if form_pessoa.is_valid():
            form_pessoa = form_pessoa.save(commit=False)
            # Arruma o campo de e-mail para não ter conflito
            if form_pessoa.email == '':
                form_pessoa.email = None

            # Arruma o campo de cpf para não ter conflito
            if form_pessoa.cpf_cnpj == '':
                form_pessoa.cpf_cnpj = None

            form_pessoa.tipopessoa = 'cliente'
            form_pessoa.save()
            url = str(request.path_info) + '?success=True'
            return HttpResponseRedirect(url)
    else:
        form_pessoa = PessoaRapidoForm()
    context = {
        "pessoaForm": form_pessoa,
        "success": success,
    }
    return render(request, "iframe/clientes/cadastro_rapido_cliente.html", context)


@login_required(login_url="/admin")
def lista_clientes(request):
    """ Página com a lista de clientes """

    # Pega informações da URL
    codigo = request.GET.get('search_cod_client', '')
    nome = request.GET.get('search_name_client', '')
    deletado = request.GET.get('deleted', False)
    page = int(request.GET.get('page', 1))

    # Filtra lista de clientes e gera páginas
    clientes = filtra_clientes(codigo, nome)  # função em funcoes.py
    paginas = Paginator(clientes, 10)
    pagina = paginas.get_page(page)
    url = arruma_url_page(request)  # função em funcoes.py

    context = {
        "pagina": pagina,
        "deletado": deletado,
        "url": url
    }
    return render(request, "iframe/clientes/lista_clientes.html", context)


@login_required(login_url="/admin")
def deletar_cliente(request, id_cliente):
    """ API para deletar um cliente """

    cliente = Pessoa.objects.get(pkid_pessoa=id_cliente)
    cliente.hide = True
    cliente.save()
    return HttpResponseRedirect("/iframe/clientes/lista?deleted=True")

@login_required(login_url="/admin")
def editar_cliente(request, id_cliente):
    
    try:
        cliente = Pessoa.objects.get(pkid_pessoa=id_cliente)
    except:
        return HttpResponseRedirect('/admin/home')

    try:
        telefone = Telefone.objects.get(fkid_pessoa=id_cliente)
        endereco = Endereco.objects.get(fkid_pessoa=id_cliente)
    except:
        telefone = Telefone(fkid_pessoa=cliente)
        endereco = Endereco(fkid_pessoa=cliente)

    success = request.GET.get('success', False)
    if request.POST:
        form_pessoa = PessoaForm(request.POST, instance=cliente)
        form_endereco = EnderecoForm(request.POST, instance=endereco)
        form_telefone = TelefoneForm(request.POST, instance=telefone)

        with transaction.atomic():
            if form_pessoa.is_valid() and form_pessoa.has_changed():
                form_pessoa.save()

            if form_endereco.is_valid() and form_endereco.has_changed():
                form_endereco.save()

            if form_telefone.is_valid() and form_telefone.has_changed():
                form_telefone.save()

            return HttpResponseRedirect(request.path_info)

    else:
        form_pessoa = PessoaForm(instance=cliente)
        form_endereco = EnderecoForm(instance=endereco)
        form_telefone = TelefoneForm(instance=telefone)

    context = {
        "cliente": cliente,
        "telefone": telefone,
        "form_pessoa": form_pessoa,
        "form_endereco": form_endereco,
        "form_telefone": form_telefone,
        "success": success
    }
    return render(request,"iframe/clientes/editar_cliente.html", context)