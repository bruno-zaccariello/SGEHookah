"""
    Módulo auxiliar com funções para views e outros
"""

from django.core.serializers import serialize
# from xml.etree import ElementTree
# import requests

from django.db.models import Q

from core.models import Produto, Pessoa

__all__ = ['filtra_produtos', 'filtra_pessoas',
           'paginar', 'arruma_url_page', 'JSON']


def arruma_url_page(request):
    """ Arruma a url de views que possuem paginação e pesquisa  """
    url = str(request.get_full_path())
    if "&page=" in url:
        url = url[:-7]
    elif url.endswith('/'):
        url += '?'
    return url


def filtra_produtos(codigo, palavra_chave):
    """ Função para fazer a filtragem de produtos """

    return Produto.objects.filter(
        Q(nomeproduto__icontains=palavra_chave) |
        Q(descricao__icontains=palavra_chave),
        codproduto__icontains=codigo,
        hide=False
    ).order_by('codproduto')


def filtra_pessoas(codigo, palavraChave):
    """ Função para fazer a filtragem de clientes """

    return Pessoa.objects.filter(
        Q(nomecompleto_razaosocial__icontains=palavraChave) |
        Q(apelido_nomefantasia=palavraChave) |
        Q(email=palavraChave),
        hide=False,
        pkid_pessoa__icontains=codigo
    ).order_by('pkid_pessoa')


def paginar(lista):
    """ Função inutilizada """
    page = 1
    ctrl = 0
    page_content = {1: []}
    for i in lista:
        page_content[page] += [i]
        ctrl += 1
        if ctrl == 10:
            ctrl = 0
            page += 1
            page_content[page] = []
    if page != 1 and not page_content[page]:
        page_content.pop(page)
    return page_content

def JSON(object):
    return serialize('json', object)

# def calcula_frete(
#     nCdEmpresa='',
#     sDsSenha='',
#     nCdServico="4014",
#     sCepOrigem="",
#     sCepDestino="",
#     nVlPeso="0.5",
#     nCdFormato=1,
#     nVlComprimento=16,
#     nVlAltura=2,
#     nVlLargura=11,
#     nVlDiametro="0",
# ):
#     """ Função para consumir a API do correios """
#     url = 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPrecoPrazo?'
#     url += f'nCdEmpresa={nCdEmpresa}'
#     url += f'&sDsSenha={sDsSenha}'
#     url += f'&nCdServico={nCdServico}'
#     url += f'&sCepOrigem={sCepOrigem}'
#     url += f'&sCepDestino={sCepDestino}'
#     url += f'&nVlPeso={nVlPeso}'
#     url += f'&nCdFormato={nCdFormato}'
#     url += f'&nVlComprimento={nVlComprimento}'
#     url += f'&nVlAltura={nVlAltura}'
#     url += f'&nVlLargura={nVlLargura}'
#     url += f'&nVlDiametro={nVlDiametro}'
#     retorno = requests.get(url)
#     tree = ElementTree.fromstring(retorno.content)
#     dici = {}
#     for child in tree.iter('*'):
#         tag = child.tag.split('}')[1]
#         dici[tag] = str(child.text)
#     return dici
