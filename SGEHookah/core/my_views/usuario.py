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

# Página do usuário


@login_required(login_url="/admin")
def change_pw_form(request):
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
    for field in form_pw:
        if field.errors:
            form_errors = True

    context = {
        "form_pw": form_pw,
        "success": success,
        "form_errors": form_errors
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
    for field in form_userInfo:
        if field.errors:
            form_errors = True

    context = {
        "form_userInfo": form_userInfo,
        "form_errors": form_errors,
        "success": success
    }
    return render(request, "usuario/forms/AlterarInfo.html", context)


@login_required(login_url="/admin")
def user_main(request):
    usuario = request.user
    context = {
        "user_usuario": usuario.get_username(),
        "user_name": usuario.get_full_name(),
        "user_email": usuario.email
    }
    return render(request, "usuario/user_main.html", context)
