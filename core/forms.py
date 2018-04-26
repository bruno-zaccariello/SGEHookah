from django import forms
#from core.models import Teste

''' class TesteForm(forms.ModelForm):
	class Meta:
		model = Teste
		fields = ['nome', 'descricao'] '''
		
class Teste(forms.Form):
	nome = forms.CharField(label='Your name', max_length=100)
	idade = forms.CharField(label='Idade', max_length=100)
	teste = forms.CharField(label='teste', max_length=100)
	teste2 = forms.CharField(label='teste2', max_length=100)
	teste3 = forms.CharField(label='teste3', max_length=100)
	teste4 = forms.CharField(label='teste4', max_length=100)
	teste5 = forms.CharField(label='teste5', max_length=100)
	teste5 = forms.CharField(label='teste5', max_length=100)
	
class FreteForm(forms.Form):
	tipo_choices = (('4014', 'Sedex'), ('4510', 'PAC'))
	nCdServico = forms.CharField(label="Serviço", widget=forms.Select(choices=tipo_choices))
	sCepOrigem = forms.CharField(label="Cep Origem", max_length=8)
	sCepDestino = forms.CharField(label="Cep Destino", max_length=8)
	nVlPeso = forms.FloatField(label="Peso")
	formato_choices = ((1, "Caixa"), (2, "Rolo/Prisma"), (3, "Envelope"))
	nCdFormato = forms.IntegerField(label="Formato", widget=forms.Select(choices=formato_choices))
	nVlLargura = forms.FloatField(label="Largura")
	nVlComprimento = forms.FloatField(label="Comprimento")
	nVlAltura = forms.FloatField(label="Altura")
	nVlDiametro = forms.FloatField(label="Diametro")
	#sCdMaoPropria
	#nVlValorDeclarado
	#sCdAvisoRecebimento