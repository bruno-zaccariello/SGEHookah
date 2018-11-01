"""
    Módulo que contem fórmularios utilizados no sistema
"""

import datetime as dt

import localflavor.br.forms as lf
from django import forms
from django.contrib.auth.models import User

import core.models as model
import ajax_select.fields as custom
from ajax_select import make_ajax_field

class CategoriaprodutoForm(forms.ModelForm):
    """ Formulário de Categoria de Produto """

    nomecategoria = forms.CharField(label="Nome da Categoria", max_length=50)

    nomecategoria.widget.attrs.update({'placeholder': '...'})

    class Meta:
        model = model.Categoriaproduto
        fields = ["nomecategoria"]


class UnidademedidaForm(forms.ModelForm):
    """ Fórmulário de Unidade de Medida """

    unidademedida = forms.CharField(label="Unidade", max_length=50)

    unidademedida.widget.attrs.update({'placeholder': '...'})

    class Meta:
        model = model.Unidademedida
        fields = ["unidademedida"]


class CadProdutoForm(forms.ModelForm):
    """ Formulário para cadastrar um produto """

    codproduto = forms.CharField(label="Código", max_length=8)
    nomeproduto = forms.CharField(label="Nome", max_length=50)
    preco = forms.DecimalField(label="Preço", max_digits=10, decimal_places=2)
    precocusto = forms.DecimalField(
        label="Preço de Custo", max_digits=10, decimal_places=2, required=False)
    sabor = forms.CharField(label="Sabor", max_length=45)
    marca = forms.CharField(label="Marca", required=False)
    altura = forms.FloatField(label="Altura (cm)")
    largura = forms.FloatField(label="Largura (cm)")
    profundidade = forms.FloatField(label="Profundidade (cm)")
    peso = forms.DecimalField(
        max_digits=10, decimal_places=3, label="Peso (Kg)")
    fkid_categoria = forms.ModelChoiceField(
        label="Categoria", queryset=model.Categoriaproduto.objects.filter(hide=False), initial=0)
    fkid_unidademedida = forms.ModelChoiceField(
        label="Unidade", queryset=model.Unidademedida.objects.filter(hide=False), initial=0)
    fotoproduto = forms.FileField(label="Escolha a Foto", required=False)
    descricao = forms.CharField(
        label="Descrição", widget=forms.Textarea, required=False)

    fotoproduto.widget.attrs.update({'class': 'FotoInput'})

    class Meta:
        model = model.Produto
        fields = ["codproduto", "preco", "sabor", "altura", "profundidade", "fkid_unidademedida",
                  "nomeproduto", "precocusto", "marca", "largura", "peso", "fkid_categoria",
                  "fotoproduto", "descricao"]


class ProdutoForm(forms.ModelForm):
    """ Formulário para editar um produto """

    codproduto = forms.CharField(label="Código", max_length=8)
    nomeproduto = forms.CharField(label="Nome")
    preco = forms.DecimalField(label="Preço", max_digits=10, decimal_places=2)
    precocusto = forms.DecimalField(
        label="Preço de Custo", max_digits=10, decimal_places=2, required=False)
    sabor = forms.CharField(label="Sabor")
    marca = forms.CharField(label="Marca", required=False)
    altura = forms.FloatField(label="Altura")
    largura = forms.FloatField(label="Largura")
    profundidade = forms.FloatField(label="Profundidade")
    peso = forms.DecimalField(max_digits=10, decimal_places=3, label="Peso")
    fkid_categoria = forms.ModelChoiceField(
        label="Categoria", queryset=model.Categoriaproduto.objects.filter(hide=False), initial=0)
    fkid_unidademedida = forms.ModelChoiceField(
        label="Unidade", queryset=model.Unidademedida.objects.filter(hide=False), initial=0)
    totalestoque = forms.FloatField(label="Estoque")
    fotoproduto = forms.FileField(label="Escolha a Foto", required=False)
    descricao = forms.CharField(
        label="Descrição", widget=forms.Textarea, required=False)

    descricao.widget.attrs.update({'class': 'Descricao'})
    fotoproduto.widget.attrs.update({'class': 'FotoInput'})
    altura.widget.attrs.update({'placeholder': 'Em cm'})
    largura.widget.attrs.update({'placeholder': 'Em cm'})
    profundidade.widget.attrs.update({'placeholder': 'Em cm'})
    peso.widget.attrs.update({'placeholder': 'Em kg'})

    class Meta:
        model = model.Produto
        fields = [
            "codproduto", "nomeproduto", "preco",
            "precocusto", "sabor", "marca",
            "altura", "largura", "profundidade",
            "peso", "fkid_unidademedida", "fkid_categoria",
            "totalestoque", "fotoproduto", "descricao"
        ]


class FormulaprodutoForm(forms.ModelForm):
    """ Formulário de fórmula de produto para página do produto """

    tempomaturacao = forms.TimeField(
        label="Tempo em Maturação", initial='00:00:00')

    class Meta:
        model = model.Formulaproduto
        fields = ["tempomaturacao"]


class FormulaCompletaForm(forms.ModelForm):
    """ Formulário de fórmula para página individual da formula """

    tempomaturacao = forms.TimeField(
        label="Tempo em Maturação", initial='00:00:00')
    fkid_produto = forms.ModelChoiceField(
        label="Produto", queryset=model.Produto.objects.filter(hide=False))

    class Meta:
        model = model.Formulaproduto
        fields = ["tempomaturacao", "fkid_produto"]


class FormulamateriaForm(forms.ModelForm):
    """ Formulário para linha de matéria prima de uma Fórmula """

    fkid_materiaprima = forms.ModelChoiceField(
        label="Matéria Prima",
        queryset=model.Materiaprima.objects.filter(hide=False),
        required=True)
    quantidade = forms.FloatField(label="Quantidade", required=True)
    unidade = forms.ModelChoiceField(
        label="Unidade",
        queryset=model.Unidademedida.objects.filter(hide=False), required=True)

    class Meta:
        model = model.Formulamateria
        fields = ["fkid_materiaprima", "quantidade", "unidade"]


class MateriaPrimaForm(forms.ModelForm):
    """ Formulário para matéria-prima """

    materiaprima = forms.CharField(label="Matéria Prima", max_length=60)
    marca = forms.CharField(label="Marca", max_length=50, required=False)
    totalestoque = forms.IntegerField(label="Estoque")
    unidade = forms.ModelChoiceField(
        label="Unidade", queryset=model.Unidademedida.objects.filter(hide=False), initial=0)

    class Meta:
        model = model.Materiaprima
        fields = ["materiaprima", "marca", "totalestoque", "unidade"]


class FreteForm(forms.Form):
    """ Formulário para calcular frete """

    tipo_choices = (('4014', 'Sedex'), ('4510', 'PAC'))
    nCdServico = forms.CharField(
        label="Serviço", widget=forms.Select(choices=tipo_choices))
    formato_choices = ((1, "Caixa"), (2, "Rolo/Prisma"), (3, "Envelope"))
    nCdFormato = forms.IntegerField(
        label="Formato", widget=forms.Select(choices=formato_choices))
    sCepOrigem = forms.IntegerField(
        label="Cep Origem", widget=forms.NumberInput(attrs={'placeholder': '0000000'}))
    sCepDestino = forms.IntegerField(
        label="Cep Destino", widget=forms.NumberInput(attrs={'placeholder': '0000000'}))
    nVlPeso = forms.FloatField(label="Peso", widget=forms.NumberInput(
        attrs={'placeholder': 'Peso em Kg'}))
    nVlLargura = forms.FloatField(label="Largura", widget=forms.NumberInput(
        attrs={'placeholder': 'Largura em cm'}))
    nVlComprimento = forms.FloatField(label="Comprimento", widget=forms.NumberInput(
        attrs={'placeholder': 'Comprimento em cm'}))
    nVlAltura = forms.FloatField(label="Altura", widget=forms.NumberInput(
        attrs={'placeholder': 'Altura em cm'}))
    #nVlDiametro = forms.FloatField(label="Diametro")
    # sCdMaoPropria
    # nVlValorDeclarado
    # sCdAvisoRecebimento


class UpdateInfoForm(forms.ModelForm):
    """ Formulário para atualizar informações de um usuário """

    email = forms.EmailField(label="E-mail", required=True)
    first_name = forms.CharField(label="Nome", required=True)
    last_name = forms.CharField(label="Sobrenome", required=True)

    class Meta:
        model = model.User
        fields = ('email', 'first_name', 'last_name')

    def clean_email(self):
        """ Confirma se o email já existe no banco de dados """

        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError('Esse e-mail já está em uso.')
        return email

    def save(self, commit=True):
        user = super(UpdateInfoForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EnderecoForm(forms.ModelForm):
    """ Formulário de endereço """

    cep = forms.CharField(label="CEP", max_length=9)
    logradouro = forms.CharField(label="Endereço", max_length=200)
    endereco_numero = forms.IntegerField(label="Número", required=False)
    complemento = forms.CharField(
        label="Complemento", max_length=20, required=False)
    bairro = forms.CharField(label="Bairro", max_length=100)
    cidade = forms.CharField(label="Cidade", max_length=150)
    uf = lf.BRStateChoiceField(label="UF")

    class Meta:
        model = model.Endereco
        fields = [
            'cep', 'logradouro', 'endereco_numero',
            'complemento', 'bairro', 'cidade',
            'uf'
        ]


class TelefoneForm(forms.ModelForm):
    """ Formulário para Telefone """

    numero = forms.CharField(label='Telefone', max_length=15, required=False)

    class Meta:
        model = model.Telefone
        fields = ['numero']


class PessoaForm(forms.ModelForm):
    """ Formulário para cadastro de uma nova pessoa """

    genero_choices = (('H', 'Homem'), ('M', 'Mulher'), ('O', 'Outro'))

    nomecompleto_razaosocial = forms.CharField(label="Nome", max_length=150)
    apelido_nomefantasia = forms.CharField(
        label="Apelido", required=False, max_length=150)
    email = forms.EmailField(label="E-mail", required=False)
    cpf_cnpj = lf.BRCPFField(label="CPF")
    rg_ie = forms.CharField(label="RG", required=False, max_length=50)
    dt_nascimento = forms.DateField(
        label="Nascimento", required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    genero = forms.CharField(label="Gênero", widget=forms.Select(
        choices=genero_choices), initial=0)

    class Meta:
        model = model.Pessoa
        fields = ['nomecompleto_razaosocial', 'apelido_nomefantasia',
                  'email', 'cpf_cnpj', 'rg_ie', 'dt_nascimento', 'genero']


class PessoaRapidoForm(forms.ModelForm):
    """ Formulário para cadastro rápido de uma pessoa """

    genero_choices = (('H', 'Homem'), ('M', 'Mulher'), ('O', 'Outro'))

    nomecompleto_razaosocial = forms.CharField(label="Nome", max_length=150)
    email = forms.EmailField(label="E-mail", required=False)
    cpf_cnpj = lf.BRCPFField(label="CPF", required=False)
    genero = forms.CharField(label="Gênero", widget=forms.Select(
        choices=genero_choices), initial=0)

    class Meta:
        model = model.Pessoa
        fields = ['nomecompleto_razaosocial', 'email', 'cpf_cnpj', 'genero']


class PedidofabricacaoForm(forms.ModelForm):
    """ Formulário para um novo pedido de fabricação """

    fkid_formula = forms.ModelChoiceField(
        label="Fórmula",
        queryset=model.Formulaproduto.objects.filter(hide=False))
    fkid_statusfabricacao = forms.ModelChoiceField(
        label="Status",
        queryset=model.Statusfabricacao.objects.filter(hide=False).order_by('order'),
        initial=0)
    lote = forms.CharField(label='Lote', max_length=8)
    quantidade = forms.FloatField(label='Quantidade a Produzir')
    dt_fim_maturacao = forms.DateTimeField(
        label='Dt. Maturação', widget=forms.HiddenInput(), initial=dt.datetime.now())

    def clean_dt_fim_maturacao(self):
        """ Realiza o cálculo para quando será o fim da maturação """

        formula_time = str(
            self.cleaned_data["fkid_formula"].tempomaturacao).split(":")
        hours = int(formula_time[0])
        minutes = int(formula_time[1])
        seconds = int(formula_time[2])

        data = dt.datetime.now() + dt.timedelta(hours=hours,
                                                minutes=minutes, seconds=seconds)
        return data

    def get_materials(self):
        """ Busca materiais de uma dada fórmula """

        materials = Formulamateria.objects.filter(
            fkid_formulaproduto=self.fkid_formula)
        return materials

    class Meta:
        model = model.Pedidofabricacao
        fields = ['fkid_formula', 'fkid_statusfabricacao',
                  'quantidade', 'dt_fim_maturacao', 'lote']

class PedidoVendaForm(forms.ModelForm):
    """ Formulário do pedido de venda """

    fkid_cliente =make_ajax_field(
        model.Pessoa, 
        'nomecompleto_razaosocial', 
        'cliente',
        required=True)
    dt_pedido = forms.DateTimeField()
    dt_pagamento = forms.DateTimeField()
    dt_preventrega = forms.DateTimeField()
    pago = forms.BooleanField()

    class Meta:
        model = model.Pedidovenda
        fields = ['fkid_cliente', 'fkid_status', 'fkid_formapag',
         'dt_pagamento', 'dt_preventrega' ,'pago']

class ItemVendaForm(forms.ModelForm):
    """ Formulário de item de venda """

    # fkid_produto = custom.AutoCompleteSelectField('produto', help_text=None)
    fkid_produto = make_ajax_field(model.Produto, 'nomeproduto', 'produto')

    class Meta:
        model = model.Itemvenda
        fields = ['fkid_produto', 'quantidade', 'vl_unitario',
                'vl_total']