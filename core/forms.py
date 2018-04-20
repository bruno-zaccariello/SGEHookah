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