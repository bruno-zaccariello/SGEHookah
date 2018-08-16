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

def lista_formula(request):
    formulas = Formulaproduto.objects.filter(hide=False)
    page = int(request.GET.get('page', 1))

    paginas = Paginator(formulas, 10)
    pagina = paginas.get_page(page)

    url = arruma_url_page(request)
    context = {
        "pagina":pagina,
        "url":url
    }
    return render(request, 'iframe/producao/formula/lista_formulas.html', context)