"""
    Módulo que contêm as views de usuário
"""

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from core.funcoes import arruma_url_page
from core.models import *
from core.forms import *


@login_required(login_url="/admin")
def change_pw_form(request):
    """ Pagina para trocar senha do user """
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
    """ Página para atualizar as infos de login do usuário """

    success = request.GET.get('success', False)
    if request.method == 'POST':
        form_user_info = UpdateInfoForm(request.POST, instance=request.user)
        if form_user_info.is_valid():
            user = form_user_info.save()
            update_session_auth_hash(request, user)
            url = str(request.path_info) + str('?success=True')
            return HttpResponseRedirect(url)
    else:
        form_user_info = UpdateInfoForm(instance=request.user)

    # Checa se existe algum erro para ativar no template
    form_errors = False
    for field in form_user_info:
        if field.errors:
            form_errors = True

    context = {
        "form_user_info": form_user_info,
        "form_errors": form_errors,
        "success": success
    }
    return render(request, "usuario/forms/AlterarInfo.html", context)


@login_required(login_url="/admin")
def user_main(request):
    """ Página do usuário """

    usuario = request.user
    context = {
        "user_usuario": usuario.get_username(),
        "user_name": usuario.get_full_name(),
        "user_email": usuario.email
    }
    return render(request, "usuario/user_main.html", context)
