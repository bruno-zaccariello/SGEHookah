import datetime
import requests

from django.shortcuts import render, redirect
from django.http import request, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.db.models import Q
from core.forms import *
from core.models import Produto, Pessoa
from xml.etree import ElementTree


__all__ = ['filtra_produtos', 'filtra_clientes',
           'paginar', 'calculoFrete', 'arruma_url_page']


def arruma_url_page(request):
    url = str(request.get_full_path())
    if "&page=" in url:
        url = url[:-7]
    elif url.endswith('/'):
        url += '?'
    return url


def filtra_produtos(codigo, palavra_chave):
    produtos = []
    if codigo == '':
        codigo = None
    if palavra_chave == '':
        palavra_chave = None

    if codigo and not palavra_chave:
        return Produto.objects.filter(hide=False, codproduto=codigo).order_by('codproduto')
    elif palavra_chave and not codigo:
        return Produto.objects.filter(hide=False,
            Q(nomeproduto__icontains=palavra_chave)
            | Q(descricao__icontains=palavra_chave)
            ).order_by('codproduto')
    elif palavra_chave and codigo:
        return Produto.objects.filter(hide=False,
            Q(nomeproduto__icontains=palavra_chave) |
            Q(descricao__icontains=palavra_chave) |
            Q(codproduto__icontains=codigo)
            ).order_by('codproduto')
    else:
        return Produto.objects.filter(hide=False).order_by('codproduto')


def filtra_clientes(codigo, nome):
    clientes=[]
    if codigo in ('', None):
        codigo=False
    if nome in ('', None):
        nome=False
    if not codigo and not nome:
        for cliente in Pessoa.objects.filter(tipopessoa = 'cliente'):
            if cliente.hide != True:
                clientes.append(cliente)
    else:
        if codigo and not nome:
            try:
                cliente=Pessoa.objects.get(pkid_pessoa = codigo)
                if cliente and cliente.hide != True:
                    clientes.append(cliente)
            except:
                pass
        elif codigo and nome:
            cliente=Pessoa.objects.get(pkid_pessoa = codigo)
            if nome.lower() in cliente.nomecompleto_razaosocial.lower():
                if cliente.hide != True:
                    clientes.append(cliente)
        elif nome and not codigo:
            for cliente in Pessoa.objects.all():
                if nome.lower() in cliente.nomecompleto_razaosocial.lower():
                    if cliente.hide != True:
                        clientes.append(cliente)
    return clientes


def paginar(lista):
    page=1
    ctrl=0
    page_content={1: []}
    for i in lista:
        page_content[page] += [i]
        ctrl += 1
        if ctrl == 10:
            ctrl=0
            page += 1
            page_content[page]=[]
    if page != 1 and not page_content[page]:
        page_content.pop(page)
    return page_content


def calculoFrete(
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
    url='http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPrecoPrazo?nCdEmpresa=&sDsSenha='
    url += '&nCdServico={}'.format(self.nCdServico)
    url += '&sCepOrigem={}'.format(self.sCepOrigem)
    url += '&sCepDestino={}'.format(self.sCepDestino)
    url += '&nVlPeso={}'.format(self.nVlPeso)
    url += '&nCdFormato={}'.format(self.nCdFormato)
    url += '&nVlComprimento={}'.format(self.nVlComprimento)
    url += '&nVlAltura={}'.format(self.nVlAltura)
    url += '&nVlLargura={}'.format(self.nVlLargura)
    url += '&nVlDiametro={}'.format(self.nVlDiametro)
    retorno=requests.get(url)
    tree=ElementTree.fromstring(retorno.content)
    dici={}
    for child in tree.iter('*'):
        tag=child.tag.split('}')[1]
        dici[tag]=str(child.text)
    return dici
