from django import forms
from django.contrib.auth.models import User
from core.models import *
from localflavor.br.forms import *
#from core.models import Teste

''' class TesteForm(forms.ModelForm):
	nome = forms.CharField(widget=forms.TextInput(attrs={'class':'codProdutoInput'}))
	
	nome.widget.attrs.update({'class':'Descricao'})
	
	class Meta:
		model = Teste
		fields = ['nome', 'descricao'] '''
		
__all__ = ['Teste', 'FreteForm', 'CadProdutoForm', 'ProdutoForm', 'UpdateInfoForm', 'CategoriaprodutoForm', 'UnidademedidaForm', 'PessoaForm', 'EnderecoForm', 'TelefoneForm',
'PessoaRapidoForm', 'MateriaPrimaForm', "FormulaprodutoForm", "Formula_materiaForm"]

class CategoriaprodutoForm(forms.ModelForm):
	nomecategoria = forms.CharField(label="Nome da Categoria", max_length=50)
	
	nomecategoria.widget.attrs.update({'placeholder':'...'})

	class Meta :
		model = Categoriaproduto
		fields = ["nomecategoria"]
		

class UnidademedidaForm(forms.ModelForm):
	unidademedida = forms.CharField(label="Unidade", max_length=50)
	
	unidademedida.widget.attrs.update({'placeholder':'...'})

	class Meta :
		model = Unidademedida
		fields = ["unidademedida"]
		

class CadProdutoForm(forms.ModelForm):
	codproduto = forms.CharField(label="Código", max_length=8)
	nomeproduto = forms.CharField(label="Nome", max_length=50)
	preco = forms.DecimalField(label="Preço", max_digits=10, decimal_places=2)
	precocusto = forms.DecimalField(label="Preço de Custo", max_digits=10, decimal_places=2, required=False)
	sabor = forms.CharField(label="Sabor", max_length=45)
	marca = forms.CharField(label="Marca", required=False)
	altura = forms.FloatField(label="Altura (cm)")
	largura = forms.FloatField(label="Largura (cm)")
	profundidade = forms.FloatField(label="Profundidade (cm)")
	peso = forms.DecimalField(max_digits=10, decimal_places=3, label="Peso (Kg)")
	fkid_categoria = forms.ModelChoiceField(label="Categoria", queryset=Categoriaproduto.objects.filter(hide=False), initial=0)
	fkid_unidademedida = forms.ModelChoiceField(label="Unidade", queryset=Unidademedida.objects.filter(hide=False), initial=0)
	fotoproduto = forms.FileField(label="Escolha a Foto", required=False)
	descricao = forms.CharField(label="Descrição", widget=forms.Textarea, required=False)
	
	fotoproduto.widget.attrs.update({'class':'FotoInput'})

	class Meta:
		model = Produto
		fields = ["codproduto", "preco", "sabor", "altura", "profundidade", "fkid_unidademedida",
		"nomeproduto", "precocusto", "marca", "largura", "peso", "fkid_categoria",
		"fotoproduto", "descricao"]
		

class ProdutoForm(forms.ModelForm):
	codproduto = forms.CharField(label="Código", max_length=8)
	nomeproduto = forms.CharField(label="Nome")
	preco = forms.DecimalField(label="Preço", max_digits=10, decimal_places=2)
	precocusto = forms.DecimalField(label="Preço de Custo", max_digits=10, decimal_places=2, required=False)
	sabor = forms.CharField(label="Sabor")
	marca = forms.CharField(label="Marca", required=False)
	altura = forms.FloatField(label="Altura")
	largura = forms.FloatField(label="Largura")
	profundidade = forms.FloatField(label="Profundidade")
	peso = forms.DecimalField(max_digits=10, decimal_places=3, label="Peso")
	fkid_categoria = forms.ModelChoiceField(label="Categoria", queryset=Categoriaproduto.objects.filter(hide=False), initial=0)
	fkid_unidademedida = forms.ModelChoiceField(label="Unidade", queryset=Unidademedida.objects.filter(hide=False), initial=0)
	totalestoque = forms.FloatField(label="Estoque")
	fotoproduto = forms.FileField(label="Escolha a Foto", required=False)
	descricao = forms.CharField(label="Descrição", widget=forms.Textarea, required=False)
    
	descricao.widget.attrs.update({'class':'Descricao'})
	fotoproduto.widget.attrs.update({'class':'FotoInput'})
	altura.widget.attrs.update({'placeholder':'Em cm'})
	largura.widget.attrs.update({'placeholder':'Em cm'})
	profundidade.widget.attrs.update({'placeholder':'Em cm'})
	peso.widget.attrs.update({'placeholder':'Em kg'})
	
	class Meta:
		model = Produto
		fields = ["codproduto", "nomeproduto", "preco", "precocusto", "sabor",
		"marca","altura", "largura", "profundidade", "peso","fkid_unidademedida" ,"fkid_categoria", "totalestoque",
		"fotoproduto", "descricao"]


class FormulaprodutoForm(forms.ModelForm):
	tempomaturacao = forms.TimeField()

	class Meta:
		model = Formulaproduto
		fields = ["tempomaturacao"]


class Formula_materiaForm(forms.ModelForm):
	fkid_materiaprima = forms.ModelChoiceField(
		label="Matéria Prima",
		queryset=Materiaprima.objects.filter(hide=False),
		required=True)
	quantidade = forms.FloatField(label="Quantidade", required=True)
	unidade = forms.ModelChoiceField(
		label="Unidade",
		queryset=Unidademedida.objects.filter(hide=False), required=True)


	class Meta:
		model = Formula_materia
		fields = ["fkid_materiaprima", "quantidade", "unidade"]


class MateriaPrimaForm(forms.ModelForm):
	materiaprima = forms.CharField(label="Matéria Prima", max_length=60)
	marca = forms.CharField(label="Marca", max_length=50, required=False)
	totalestoque = forms.IntegerField(label="Estoque")
	unidade = forms.ModelChoiceField(label="Unidade", queryset=Unidademedida.objects.filter(hide=False), initial=0)

	class Meta:
		model = Materiaprima
		fields = ["materiaprima", "marca", "totalestoque", "unidade"]



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
    nVlAltura = forms.FloatField(label="Altura",   widget=forms.NumberInput(attrs={'placeholder': 'Altura em cm'}))
	#nVlDiametro = forms.FloatField(label="Diametro")
	#sCdMaoPropria
	#nVlValorDeclarado
	#sCdAvisoRecebimento
	

class UpdateInfoForm(forms.ModelForm):
	email = forms.EmailField(label="E-mail", required=True)
	first_name = forms.CharField(label="Nome", required=True)
	last_name = forms.CharField(label="Sobrenome", required=True)
	
	class Meta :
		model = User
		fields = ('email', 'first_name', 'last_name')
		
	def clean_email(self):
		email = self.cleaned_data.get('email')
		if email and User.objects.filter(email=email).count():
			raise forms.ValidationError('Esse e-mail já está em uso.')
		return email
			
	def save(self, commit=True):
		user = super(UpdateInfoForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		
		if commit :
			user.save()
			
		return user

class EnderecoForm(forms.ModelForm):
    cep = forms.CharField(label="CEP", max_length=9)
    logradouro = forms.CharField(label="Endereço", max_length=200)
    numero = forms.IntegerField(label="Número", required=False)
    complemento = forms.CharField(label="Complemento", max_length=20, required=False)
    bairro = forms.CharField(label="Bairro", max_length=100)
    cidade = forms.CharField(label="Cidade", max_length=150)
    uf = BRStateChoiceField(label="UF")
    
    class Meta :
        model = Endereco
        fields = ['cep', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'uf']

class TelefoneForm(forms.ModelForm):
    numero = forms.CharField(label='Telefone', max_length=15, required=False)
    
    class Meta :
        model = Telefone
        fields = ['numero']
        
class PessoaForm(forms.ModelForm):
    genero_choices = (('H', 'Homem'), ('M', 'Mulher'), ('O', 'Outro'))

    nomecompleto_razaosocial = forms.CharField(label="Nome", max_length=150)
    apelido_nomefantasia = forms.CharField(label="Apelido", required=False, max_length=150)
    email = forms.EmailField(label="E-mail", required=False)
    cpf_cnpj = BRCPFField(label="CPF")
    rg_ie = forms.CharField(label="RG", required=False, max_length=50)
    dt_nascimento = forms.DateField(label="Nascimento", required=False, widget=forms.DateInput(attrs={'type':'date'}))
    genero = forms.CharField(label="Gênero", widget=forms.Select(choices=genero_choices), initial=0)
    

    class Meta:
        model = Pessoa
        fields = ['nomecompleto_razaosocial', 'apelido_nomefantasia', 'email', 'cpf_cnpj', 'rg_ie', 'dt_nascimento', 'genero']
        
class PessoaRapidoForm(forms.ModelForm):
    genero_choices = (('H', 'Homem'), ('M', 'Mulher'), ('O', 'Outro'))

    nomecompleto_razaosocial = forms.CharField(label="Nome", max_length=150)
    email = forms.EmailField(label="E-mail", required=False)
    cpf_cnpj = BRCPFField(label="CPF", required=False)
    genero = forms.CharField(label="Gênero", widget=forms.Select(choices=genero_choices), initial=0)

    class Meta:
        model = Pessoa
        fields = ['nomecompleto_razaosocial', 'email', 'cpf_cnpj', 'genero']