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

@login_required(login_url="/admin")
def cadastrar_materia(request):
	success = request.GET.get('success', False)
	if request.POST:
		form = MateriaPrimaForm(request.POST)
		if form.is_valid():
			form.save()
			url = str(request.path_info) + str('?success=True')
			return HttpResponseRedirect(url)
	else:
		form = MateriaPrimaForm()
	context = {
		'form':form,
		'success':success
	}
	return render(request, 'iframe/producao/cadastrar_materia.html', context)

@login_required(login_url="/admin")
def lista_materia(request):
	deletado = request.GET.get('deleted', False)
	page = int(request.GET.get('page', 1))

	lista_materias = Materiaprima.objects.filter(hide=False)
	paginas = Paginator(lista_materias, 10)
	materias = paginas.get_page(page)

	url = arruma_url_page(request)
	context = {
		"pagina":materias,
		"deletado":deletado,
		"url":url,
	}
	return render(request, 'iframe/producao/lista_materia.html', context)