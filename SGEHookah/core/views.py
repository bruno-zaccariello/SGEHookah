import datetime
import requests

from django.shortcuts import render, redirect
from django.http import request, HttpResponse, HttpResponseRedirect, JsonResponse
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

from core.my_views.clientes import *
from core.my_views.produtos import *
from core.my_views.usuario import *
from core.my_views.producao import *
from core.custom.ajax_requests import *

# Create your views here.
	
def index(request):
	return render(request, "index.html")

#Home e Principais	
	
@login_required(login_url="/admin")
def home(request):
	return render(request, "base.html")	

@login_required(login_url="/admin")
def redirect_home(request):
	return redirect('/admin/home')

@login_required(login_url="/admin")
def iframe_home(request):

	# Info sobre pedidos de fabricação

	fab_pedidos = Pedidofabricacao.objects.filter(
			hide=False
		).exclude(
			fkid_statusfabricacao__order=3
		).order_by(
			'-fkid_statusfabricacao', 'dt_fim_maturacao'
		)

	context = {
		"fab_pedidos":fab_pedidos
	}
	return render(request, "iframe/home.html", context)	

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