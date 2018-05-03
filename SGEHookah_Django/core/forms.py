from django import forms
from core.models import AuthUser
#from core.models import Teste

''' class TesteForm(forms.ModelForm):
	class Meta:
		model = Teste
		fields = ['nome', 'descricao'] '''
		
__all__ = ['Teste', 'FreteForm', 'UpdateInfoForm']
		
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
	formato_choices = ((1, "Caixa"), (2, "Rolo/Prisma"), (3, "Envelope"))
	nCdFormato = forms.IntegerField(label="Formato", widget=forms.Select(choices=formato_choices))
	sCepOrigem = forms.IntegerField(label="Cep Origem", widget=forms.NumberInput(attrs={'placeholder': '0000000'}))
	sCepDestino = forms.IntegerField(label="Cep Destino", widget=forms.NumberInput(attrs={'placeholder': '0000000'}))
	nVlPeso = forms.FloatField(label="Peso", widget=forms.NumberInput(attrs={'placeholder': 'Peso em Kg'}))
	nVlLargura = forms.FloatField(label="Largura", widget=forms.NumberInput(attrs={'placeholder': 'Largura em cm'}))
	nVlComprimento = forms.FloatField(label="Comprimento", widget=forms.NumberInput(attrs={'placeholder': 'Comprimento em cm'}))
	nVlAltura = forms.FloatField(label="Altura", widget=forms.NumberInput(attrs={'placeholder': 'Altura em cm'}))
	#nVlDiametro = forms.FloatField(label="Diametro")
	#sCdMaoPropria
	#nVlValorDeclarado
	#sCdAvisoRecebimento
	
class UpdateInfoForm(forms.ModelForm):
	email = forms.EmailField(label="E-mail", required=True)
	first_name = forms.CharField(label="Nome", required=False)
	last_name = forms.CharField(label="Sobrenome", required=False)
	
	class Meta :
		model = AuthUser
		fields = ('email', 'first_name', 'last_name')
		
	def clean_email(self):
		email = self.cleaned_data.get('email')
		if email and AuthUser.objects.filter(email=email).count():
			raise forms.ValidationError('Esse e-mail já está em uso.')
		return email
	
	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		
		if commit :
			user.save()
			
		return user
