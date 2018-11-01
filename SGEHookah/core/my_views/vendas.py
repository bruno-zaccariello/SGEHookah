import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import inlineformset_factory
from django.views import View
from django.views.generic import TemplateView

from core.funcoes import arruma_url_page

import core.models as models
import core.forms as forms

class NovaVenda(TemplateView):
    template_name = 'iframe/vendas/nova_venda.html'
    formset_itemsVenda = inlineformset_factory(
        models.Pedidovenda,
        models.Itemvenda,
        extra=0,
        min_num=1,
        exclude=['hide'],
        form=forms.ItemVendaForm
        )

    def get(self, request):
        vendaForm = forms.PedidoVendaForm()
        itemsForms = self.formset_itemsVenda() 
        context = {
            'vendaForm':vendaForm,
            'itemsForms':itemsForms
        }
        return render(request, self.template_name, context)

    def post(self, request):
        vendaForm = forms.PedidoVendaForm(request.POST)
        with transaction.atomic():
            if vendaForm.is_valid():
                vendaForm = vendaForm.save(commit=False)
                vendaForm.dt_pedido = datetime.datetime.now()
                vendaForm.fkid_usuario = request.user.id
                vendaForm.save()
                itemsForms = self.formset_itemsVenda(request.POST, instance=vendaForm)
                if itemsForms.is_valid():
                    itemsForms = itemsForms.save()
                    return render(request, self.template_name, context)
        return render(request, self.template_name)