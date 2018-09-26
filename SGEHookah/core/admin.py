"""
    Módulo que contém os modelos editáveis no 
    admin do próprio django
"""

from django.contrib import admin
from core.models import *

# register your models here.

admin.site.register(Categoriaproduto)
admin.site.register(Produto)
admin.site.register(Unidademedida)
admin.site.register(Pessoa)
admin.site.register(Endereco)
admin.site.register(Telefone)
admin.site.register(Formulaproduto)
admin.site.register(Formulamateria)
admin.site.register(Materiaprima)
admin.site.register(Pedidofabricacao)
admin.site.register(Statusfabricacao)
admin.site.register(Pedidovenda)
admin.site.register(Statusvenda)
admin.site.register(Formapagamento)
