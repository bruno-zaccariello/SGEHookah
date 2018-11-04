from json import loads as load_json

from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.serializers import serialize
from django.forms.models import model_to_dict

import core.forms as forms
import core.models as models
from core.funcoes import *


def ajax_nova_fabricacao(request):
    """
        Função utilizada para atualizar a lista de matérias-primas
        em uma fabricação (ao alterar o campo de fórmula utilizada)
    """
    lista = []
    if request.GET:
        rget = request.GET

        try:
            formula = models.Formulaproduto.objects.get(
                pkid_formula=rget.get('formula_id'))
        except:
            formula = False

        if formula:
            for item in models.Formulamateria.objects.filter(fkid_formulaproduto=formula).values():
                id_materia = item['fkid_materiaprima_id']
                unidade = item['unidade_id']
                # Pega o nome da materiaprima invés do id
                item['fkid_materiaprima_id'] = models.Materiaprima.objects.get(
                    pkid_materiaprima=id_materia
                ).materiaprima
                # Pega o nome da unidademedida invés do id
                item['unidade_id'] = models.Unidademedida.objects.get(
                    pkid_unidademedida=unidade
                ).unidademedida

                lista.append((item, id_materia))

    data = {
        'response': True if formula and len(lista) > 0 else False,
        'lista': lista
    }

    return JsonResponse(data)


def ajax_checa_materias(request):
    """
        Função utilizada para checar a quantidade de materiais
        em um pedido de fabricação
    """
    try:
        rdata = []
        if request.body:
            rget = load_json(request.body)

            for id_materia, quantity in rget.get('materias_ids'):
                materia = models.Materiaprima.objects.get(
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

def get_produto(request):
    data = {'produto':False}
    if request.body:
        rget = load_json(request.body)
        produto = models.Produto.objects.filter(
                pkid_produto = rget.get('produto')
            )
        data = serialize(
            'json',
            produto
        )
        return JsonResponse(data, safe=False)

def search_produto(request):
    data = {'produto':False}
    if request.body:
        rget = load_json(request.body)
        produto = models.Produto.objects.filter(
                nomeproduto = rget.get('produto')
            )
        data = serialize(
            'json',
            produto
        )
        return JsonResponse(data, safe=False)

def get_clientes(request):
    clientes = models.Pessoa.objects.filter(
        hide=False
    ).values()
    return JsonResponse(clientes, safe=False)