import datetime
import requests
import json

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


def ajax_nova_fabricacao(request):
    lista = []
    if request.GET:
        rget = request.GET

        try:
            formula = Formulaproduto.objects.get(
                pkid_formula=rget.get('formula_id'))
        except:
            formula = False

        if formula:
            for item in Formulamateria.objects.filter(fkid_formulaproduto=formula).values():
                id_materia = item['fkid_materiaprima_id']
                unidade = item['unidade_id']
                # Pega o nome da materiaprima invés do id
                item['fkid_materiaprima_id'] = Materiaprima.objects.get(
                    pkid_materiaprima=id_materia
                ).materiaprima
                # Pega o nome da unidademedida invés do id
                item['unidade_id'] = Unidademedida.objects.get(
                    pkid_unidademedida=unidade
                ).unidademedida

                lista.append((item, id_materia))

    data = {
        'response': True if formula and len(lista) > 0 else False,
        'lista': lista
    }

    return JsonResponse(data)


def ajax_checa_materias(request):
    try:
        rdata = []
        if request.body:
            rget = json.loads(request.body)

            for id_materia, quantity in rget.get('materias_ids'):
                materia = Materiaprima.objects.get(
                    pkid_materiaprima=id_materia)
                if materia.totalestoque >= quantity:
                    rdata.append((id_materia, True))
                else:
                    rdata.append((id_materia, False))

        data = {
            'response': True,
            'checks': rdata
        }
    except:
        data = {
            'response': False,
            'checks': []
        }
    print(data)
    return JsonResponse(data)
