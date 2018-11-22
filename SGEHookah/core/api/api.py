from json import loads as load_json

from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.serializers import serialize
from django.forms.models import model_to_dict

import core.forms as forms
import core.models as models
from core.funcoes import *

def valida_fabricacao(request, id_formula):
    """
        Função utilizada para atualizar a lista de matérias-primas
        em uma fabricação (ao alterar o campo de fórmula utilizada)
    """
    try:
        formula = models.Formulaproduto.objects.filter(
            pkid_formula=id_formula
        ).values()[0]
        r_materias = models.Formulamateria.objects.filter(
            fkid_formulaproduto=formula['pkid_formula']
        )
        materias = [
            {
            'id':x.fkid_materiaprima.pk,
            'materia':x.fkid_materiaprima.materiaprima, 
            'estoque':x.fkid_materiaprima.totalestoque,
            'unidade':x.fkid_materiaprima.unidade.unidademedida,
            'quantidade':x.quantidade
            } for x in r_materias
        ]
        data = {
            'response':True,
            'formula':formula,
            'materias':materias
        }
        return JsonResponse(data, safe=False, status=200)
    except Exception:
        data = {
            'response': False,
            'error':f'Internal Server Error'
        }
        return JsonResponse(data, safe=False, status=500)

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
    data = {
        'produto': False,
        'response': False
    }
    try:
        if request.body:
            req = load_json(request.body)
        
        try:
            data = {
                'produto': models.Produto.objects.filter(
                    pkid_produto = req.get('produto')
                    ).values()[0],
                'response': True
            }
            return JsonResponse(data, safe=False, status=200)
        except Exception:
            data['error'] = f'ID Inválido\nValor Recebido: {req.get("produto")}'
            return JsonResponse(data, safe=False, status=404)
    except:
        data['error'] = 'favor contatar o administrador do sistema'
        return JsonResponse(data, safe=False, status=500)

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