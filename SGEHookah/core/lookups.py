# yourapp/lookups.py
from ajax_select import register, LookupChannel
import core.models as models

@register('produto')
class ProdutoLookup(LookupChannel):

    model = models.Produto

    def get_query(self, q, request):
        return self.model.objects.filter(nomeproduto__icontains=q).order_by('nomeproduto')

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item.nomeproduto

    def get_result(self,obj):
        u""" result is the simple text that is the completion of what the person typed """
        return obj.nomeproduto

    def format_match(self,obj):
        """ (HTML) formatted item for display in the dropdown """
        return r'%s' % str(obj.nomeproduto)

@register('cliente')
class ClienteLookup(LookupChannel):

    model = models.Pessoa

    def get_query(self, q, request):
        return self.model.objects.filter(
            nomecompleto_razaosocial__icontains=q,
            hide=False
            ).order_by('nomecompleto_razaosocial')

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item.nomecompleto_razaosocial

    def get_result(self,obj):
        u""" result is the simple text that is the completion of what the person typed """
        return obj.nomecompleto_razaosocial

    def format_match(self,obj):
        """ (HTML) formatted item for display in the dropdown """
        return r'%s' % str(obj.nomecompleto_razaosocial)