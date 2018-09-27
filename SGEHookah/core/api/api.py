from json import loads as load_json

from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse

from core.forms import *
from core.models import *
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
    """
        Função utilizada para checar a quantidade de materiais
        em um pedido de fabricação
    """
    try:
        rdata = []
        if request.body:
            rget = load_json(request.body)

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