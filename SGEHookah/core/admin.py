"""
    Módulo que contém os modelos editáveis no 
    admin do próprio django
"""

from django.contrib import admin
import core.models as models
import core.forms as forms


# register your models here.

class ItemvendaAdmin(admin.ModelAdmin):
    form = forms.ItemVendaForm


admin.site.register(models.Categoriaproduto)
admin.site.register(models.Produto)
admin.site.register(models.Unidademedida)
admin.site.register(models.Pessoa)
admin.site.register(models.Endereco)
admin.site.register(models.Telefone)
admin.site.register(models.Formulaproduto)
admin.site.register(models.Formulamateria)
admin.site.register(models.Materiaprima)
admin.site.register(models.Pedidofabricacao)
admin.site.register(models.Statusfabricacao)
admin.site.register(models.Pedidovenda)
admin.site.register(models.Statusvenda)
admin.site.register(models.Formapagamento)
admin.site.register(models.Itemvenda, ItemvendaAdmin)
