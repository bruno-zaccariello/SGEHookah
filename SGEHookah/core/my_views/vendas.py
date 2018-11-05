import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import inlineformset_factory
from django.views import View
from django.views.generic import TemplateView
from django.core.paginator import Paginator

from core.funcoes import arruma_url_page

import core.models as models
import core.forms as forms

class NovaVenda(TemplateView):
    template_name = 'iframe/vendas/nova_venda.html'
    url = '/iframe/vendas/nova/'
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
            'itemsForms':itemsForms,
            'success':request.GET.get('success'),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        vendaForm = forms.PedidoVendaForm(request.POST)
        itemsForms = self.formset_itemsVenda(request.POST)
        with transaction.atomic():
            if vendaForm.is_valid():
                vendaForm = vendaForm.save(commit=False)
                vendaForm.fkid_usuario = request.user
                vendaForm.save()
                itemsForms = self.formset_itemsVenda(request.POST, instance=vendaForm)
                if itemsForms.is_valid():
                    itemsForms = itemsForms.save()
                    return HttpResponseRedirect(self.url+'?success=True')
        context = {
            'vendaForm':vendaForm,
            'itemsForms':itemsForms
        }
        return render(request, self.template_name, context)

class ListaVendas(TemplateView):
    template_name = 'iframe/vendas/lista_vendas.html'
    url = '/iframe/vendas/'

    def get(self, request):
        page = int(request.GET.get('page', 1))
        
        vendas = models.Pedidovenda.objects.filter(hide=False).order_by('pkid_venda')
        paginas = Paginator(vendas, 10)
        pagina = paginas.get_page(page)

        context = {
            'pagina':pagina,
        }
        return render(request, self.template_name, context)