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
        if form_pessoa.is_valid() and form_endereco.is_valid() and form_telefone.is_valid():
            # Caso aja erro o atomic() irá desfazer as alteração feitas durante o código.
            with transaction.atomic():
                # Altera o tipo de pessoa no formulario e salva
                form_pessoa = form_pessoa.save(commit=False)
                form_pessoa.tipopessoa = 'cliente'
                form_pessoa.save()
                pessoa = Pessoa.objects.get(pkid_pessoa=form_pessoa.pk)

                # Atualiza o endereço com a pessoa recém criada e salva
                form_endereco = form_endereco.save(commit=False)
                form_endereco.fkid_pessoa = pessoa
                form_endereco.save()

                # Arruma o campo de telefone e salva
                form_telefone = form_telefone.save(commit=False)
                if form_telefone.numero not in ('', None):
                    form_telefone.fkid_pessoa = pessoa
                    numero = str(form_telefone.numero)
                    form_telefone.ddd = numero[1:3]
                    form_telefone.numero = numero[4:]
                    form_telefone.save()

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
        "clientes": pagina,
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
