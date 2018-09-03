from xml.etree import ElementTree
import requests

from django.db.models import Q

from core.models import Produto, Pessoa

__all__ = ['filtra_produtos', 'filtra_clientes',
           'paginar', 'calcula_frete', 'arruma_url_page']


def arruma_url_page(request):
    url = str(request.get_full_path())
    if "&page=" in url:
        url = url[:-7]
    elif url.endswith('/'):
        url += '?'
    return url


def filtra_produtos(codigo, palavra_chave):
    if codigo == '':
        codigo = None
    if palavra_chave == '':
        palavra_chave = None

    if palavra_chave and codigo:
        return Produto.objects.filter(
            Q(nomeproduto__icontains=palavra_chave) |
            Q(descricao__icontains=palavra_chave) |
            Q(codproduto__icontains=codigo),
            hide=False
        ).order_by('codproduto')
    elif codigo and not palavra_chave:
        return Produto.objects.filter(hide=False, codproduto=codigo).order_by('codproduto')
    elif palavra_chave and not codigo:
        return Produto.objects.filter(
            Q(nomeproduto__icontains=palavra_chave) |
            Q(descricao__icontains=palavra_chave),
            hide=False
        ).order_by('codproduto')
    else:
        return Produto.objects.filter(hide=False).order_by('codproduto')


def filtra_clientes(codigo, nome):
    if codigo == '':
        codigo = None
    if nome == '':
        nome = None

    if codigo and not nome:
        return Pessoa.objects.filter(
            hide=False, pkid_pessoa__icontains=codigo
        ).order_by('pkid_pessoa')
    elif nome and not codigo:
        return Pessoa.objects.filter(hide=False, nome__icontains=nome).order_by('pkid_pessoa')
    elif nome and codigo:
        return Pessoa.objects.filter(
            hide=False,
            nome__icontains=nome,
            pkid_pessoa__icontains=codigo
        ).order_by('pkid_pessoa')
    else:
        return Pessoa.objects.filter(hide=False)


def paginar(lista):
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


def calcula_frete(
        nCdEmpresa='',
        sDsSenha='',
        nCdServico="4014",
        sCepOrigem="",
        sCepDestino="",
        nVlPeso="0.5",
        nCdFormato=1,
        nVlComprimento=16,
        nVlAltura=2,
        nVlLargura=11,
        nVlDiametro="0",
    ):
    url = 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPrecoPrazo?'
    url += f'nCdEmpresa={nCdEmpresa}'
    url += f'&sDsSenha={sDsSenha}'
    url += f'&nCdServico={nCdServico}'
    url += f'&sCepOrigem={sCepOrigem}'
    url += f'&sCepDestino={sCepDestino}'
    url += f'&nVlPeso={nVlPeso}'
    url += f'&nCdFormato={nCdFormato}'
    url += f'&nVlComprimento={nVlComprimento}'
    url += f'&nVlAltura={nVlAltura}'
    url += f'&nVlLargura={nVlLargura}'
    url += f'&nVlDiametro={nVlDiametro}'
    retorno = requests.get(url)
    tree = ElementTree.fromstring(retorno.content)
    dici = {}
    for child in tree.iter('*'):
        tag = child.tag.split('}')[1]
        dici[tag] = str(child.text)
    return dici
