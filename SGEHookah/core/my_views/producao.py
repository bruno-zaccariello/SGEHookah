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
def lista_formula(request):
    formulas = Formulaproduto.objects.filter(hide=False)
    page = int(request.GET.get('page', 1))
    deletado = request.GET.get('deleted', False)

    paginas = Paginator(formulas, 10)
    pagina = paginas.get_page(page)

    url = arruma_url_page(request)
    context = {
        "pagina":pagina,
        "success":deletado,
        "url":url,
    }
    return render(request, 'iframe/producao/formula/lista_formulas.html', context)

@login_required(login_url="/admin")
def pagina_formula(request, id_formula):
    try:
        Formula = Formulaproduto.objects.filter(hide=False).get(pkid_formula=id_formula)
    except:
        Formula = None

    success = request.GET.get('success', False)

    formset_materias = inlineformset_factory(
        Formulaproduto,
        Formulamateria,
        extra=0,
        min_num=1,
        exclude=[])

    if request.POST:
        with transaction.atomic():
            form_formula = FormulaCompletaForm(request.POST, instance=Formula)
            forms_materia = formset_materias(request.POST, instance=Formula)

            if form_formula.is_valid():
                formula = form_formula.save(commit=False)
                formula.save()

                forms_materia = formset_materias(request.POST, instance=formula)

                if forms_materia.is_valid():
                    forms_materia.save()

                url = str(request.path_info) + str('?success=True')
                return HttpResponseRedirect(url)
    else:
        form_formula = FormulaCompletaForm(instance=Formula)
        forms_materia = formset_materias(instance=Formula)

    context = {
        "Formula":Formula,
        "form_formula": form_formula,
        "forms_materia": forms_materia,
        "success": success
    }
    return render(request, "iframe/producao/formula/pagina_formula.html", context)

@login_required(login_url="/admin")
def deletar_formula(request, id_formula):
    formula = Formulaproduto.objects.get(pkid_formula=id_formula)
    formula.hide = True
    formula.save()
    return HttpResponseRedirect('/iframe/producao/formulas/lista/?deleted=True')

@login_required(login_url="/admin")
def nova_fabricacao(request):
    success = request.GET.get('success', False)
    if request.POST:
        fabricaForm = PedidofabricacaoForm(request.POST)
        if fabricaForm.is_valid():
            fabricaForm.save()
            url = str(request.path_info) + '?success=True'
            return HttpResponseRedirect(url)
    else:
        fabricaForm = PedidofabricacaoForm()
    context = {
        "fabricaForm":PedidofabricacaoForm,
        "success":success,
    }
    return render(request, "iframe/producao/pedidos/nova_fabricacao.html", context)
    