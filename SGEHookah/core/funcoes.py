from django.shortcuts import render, redirect
from django.http import request, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from core.forms import *
from core.models import Produto, Pessoa
import datetime
import requests
from xml.etree import ElementTree

__all__ = ['filtra_produtos', 'filtra_clientes', 'paginar', 'calculoFrete', 'arruma_url_page']

def arruma_url_page(request):
    url = str(request.get_full_path())
    if "&page=" in url :
        url = url[:-7]
    elif url.endswith('/'):
        url += '?'
    return url

def filtra_produtos(codigo, pChave):
	produtos = []
	if codigo == '' or codigo == None :
		codigo = False
	if pChave == '' or pChave == None :
		pChave = False
	if not codigo and not pChave :
		for produto in Produto.objects.all() :
			if produto.hide != True :
				produtos.append(produto)
	else :
		if codigo and not pChave :
			try:
				produto = Produto.objects.get(codproduto=codigo)
				if produto and produto.hide != True :
					produtos.append(produto)
			except:
				pass
		elif codigo and pChave :
			item = Produto.objects.get(codproduto=codigo)
			if pChave.lower() in item.nomeproduto.lower():
				if item.hide != True :
					produtos.append(item)
			elif pChave.lower() in item.descricao.lower():
				if item.hide != True :
					produtos.append(item)
		elif pChave and not codigo :
			for produto in Produto.objects.all():
				if pChave.lower() in produto.nomeproduto.lower():
					if produto.hide != True :
						produtos.append(produto)
				elif pChave.lower() in produto.descricao.lower():
					if produto.hide != True :
						produtos.append(produto)
	return produtos

def filtra_clientes(codigo, nome):
	clientes = []
	if codigo in ('', None):
		codigo = False
	if nome in ('', None):
		nome = False
	if not codigo and not nome :
		for cliente in Pessoa.objects.filter(fkid_tipopessoa=1):
			if cliente.hide != True :
				clientes.append(cliente)
	else :
		if codigo and not nome :
			try:
				cliente = Pessoa.objects.get(pkid_pessoa=codigo)
				if cliente and cliente.hide != True :
					clientes.append(cliente)
			except:
				pass
		elif codigo and nome :
			cliente = Pessoa.objects.get(pkid_pessoa=codigo)
			if nome.lower() in cliente.nomecompleto_razaosocial.lower():
				if cliente.hide != True :
					clientes.append(cliente)
		elif nome and not codigo :
			for cliente in Pessoa.objects.all():
				if nome.lower() in cliente.nomecompleto_razaosocial.lower():
					if cliente.hide != True :
						clientes.append(cliente)
	return clientes
	
def paginar(lista):
	page = 1
	ctrl = 0
	page_content = {1:[]}
	for i in lista :
		page_content[page] += [i]
		ctrl += 1
		if ctrl == 10:
			ctrl = 0
			page += 1
			page_content[page] = []
	if page != 1 and len(page_content[page]) == 0 :
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
    url = f"http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPrecoPrazo?nCdEmpresa=&sDsSenha=&nCdServico={nCdServico}&sCepOrigem={sCepOrigem}&sCepDestino={sCepDestino}&nVlPeso={nVlPeso}&nCdFormato={nCdFormato}&nVlComprimento={nVlComprimento}&nVlAltura={nVlAltura}&nVlLargura={nVlLargura}&nVlDiametro={nVlDiametro}&sCdMaoPropria={sCdMaoPropria}&nVlValorDeclarado={nVlValorDeclarado}&sCdAvisoRecebimento={sCdAvisoRecebimento}"
    retorno = requests.get(url)
    tree = ElementTree.fromstring(retorno.content)
    dici = {}
    for child in tree.iter('*'):
        tag = child.tag.split('}')[1]
        dici[tag] = str(child.text)
    return dici	
