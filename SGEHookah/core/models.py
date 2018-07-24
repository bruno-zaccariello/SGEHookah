# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

__all__ = ["Categoriaproduto", "Produto", "Unidademedida", "Pessoa", "Endereco", "Telefone", "Formulaproduto", "Formula_materia", "Materiaprima"]

class Categoriaproduto(models.Model):
    pkid_categoria = models.AutoField(primary_key=True)  # Field name made lowercase.
    nomecategoria = models.CharField('Nome da Categoria', unique=True, max_length=100)  # Field name made lowercase.
    hide = models.BooleanField(default=0)  # Field name made lowercase.

    def __str__(self):
        return self.nomecategoria

    class Meta:
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias (Produto)'



class Cotacaocompra(models.Model):
    pkid_cotacao = models.AutoField(primary_key=True)  # Field name made lowercase.
    fornecedor = models.CharField(max_length=100, blank=True, null=True)  # Field name made lowercase.
    dt_cotacao = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    dt_entrega = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    formapamento = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    pedidocompra_pkid_compra = models.IntegerField()  # Field name made lowercase.
    statuscotacao_pkid_status = models.IntegerField()  # Field name made lowercase.
    dt_cadastro = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    hide = models.TextField( default=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True


class Endereco(models.Model):
    pkid_endereco = models.AutoField(primary_key=True)  # Field name made lowercase.
    fkid_pessoa = models.ForeignKey(
        'Pessoa', models.DO_NOTHING, 
        blank=True, null=True,
        verbose_name='Pessoa')  # Field name made lowercase.
    logradouro = models.CharField('Endereço', max_length=100)  # Field name made lowercase.
    numero = models.CharField('Número', max_length=7, null=True, blank=True)  # Field name made lowercase.
    complemento = models.CharField('Complemento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField('CEP', max_length=9)  # Field name made lowercase.
    bairro = models.CharField('Bairro', max_length=100)  # Field name made lowercase.
    cidade = models.CharField('Cidade', max_length=150)  # Field name made lowercase.
    uf = models.CharField('Estado', max_length=2)  # Field name made lowercase.
    hide = models.BooleanField(default=0)  # Field name made lowercase.

    def __str__(self):
        return  f'{self.fkid_pessoa.nomecompleto_razaosocial} : {self.cep}'

    class Meta:
        managed = True
        verbose_name = 'Endereço (Pessoa : CEP)'
        verbose_name_plural = 'Endereços'

class Entrega(models.Model):
    pkid_entrega = models.AutoField(primary_key=True)  # Field name made lowercase.
    dataentrega = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    formaentrega = models.CharField(max_length=100, blank=True, null=True)  # Field name made lowercase.
    valorfrete = models.TextField(blank=True, null=True)  # Field name made lowercase.
    nomecontarecebimento = models.CharField(max_length=100, blank=True, null=True)  # Field name made lowercase.
    fkid_usuario_alteracao = models.IntegerField()  # Field name made lowercase.
    dt_cadastro = models.DateTimeField()  # Field name made lowercase.
    dt_alteracao = models.DateTimeField()  # Field name made lowercase.
    hide = models.TextField( default=0)  # Field name made lowercase.

    class Meta:
        managed = True


class Formapagamento(models.Model):
    pkid_formapag = models.AutoField(primary_key=True)  # Field name made lowercase.
    formapagamento = models.CharField(max_length=50)  # Field name made lowercase.
    fkid_usuario_alteracao = models.IntegerField()  # Field name made lowercase.
    dt_cadastro = models.DateTimeField()  # Field name made lowercase.
    dt_alteracao = models.DateTimeField()  # Field name made lowercase.
    hide = models.TextField( default=0)  # Field name made lowercase.

    class Meta:
        managed = True


class Formulaproduto(models.Model):
    pkid_formula = models.AutoField(primary_key=True)  # Field name made lowercase.
    fkid_produto = models.ForeignKey(
        'Produto', on_delete=models.DO_NOTHING,
        verbose_name='Produto')  # Field name made lowercase.
    fkid_formula_materia = models.ManyToManyField(
        'Materiaprima', 
        through='Formula_materia',
        verbose_name='Matérias Primas'
    )
    tempomaturacao = models.TimeField('Tempo de Maturação')  # Field name made lowercase.
    hide = models.BooleanField(default=0)  # Field name made lowercase.

    def __str__(self):
        return f'Fórmula : {self.fkid_produto.nomeproduto}'

    class Meta:
        managed = True
        verbose_name = 'Fórmula : Produto'
        verbose_name_plural = 'Fórmulas (Produto)'


class Itemcompra(models.Model):
    pkid_item = models.AutoField(primary_key=True)  # Field name made lowercase.
    produto = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    descricaoproduto = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    precounitario = models.TextField(blank=True, null=True)  # Field name made lowercase.
    totalvenda = models.TextField(blank=True, null=True)  # Field name made lowercase.
    dt_cadastro = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    hide = models.TextField(default=0, blank=True, null=True)  # Field name made lowercase.
    pedidocompra_pkid_compra = models.IntegerField()  # Field name made lowercase.
    statuscompra_pkid_status = models.IntegerField()  # Field name made lowercase.
    unidademedidacompra_pkid_unidademedida = models.IntegerField()  # Field name made lowercase.

    class Meta:
        managed = True
        unique_together = (('pkid_item', 'pedidocompra_pkid_compra'),)


class Itemcotacao(models.Model):
    pkid_item = models.AutoField(primary_key=True)  # Field name made lowercase.
    produto = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    descricaoproduto = models.CharField(max_length=100, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    precounitario = models.TextField(blank=True, null=True)  # Field name made lowercase.
    totalvenda = models.TextField(blank=True, null=True)  # Field name made lowercase.
    dt_cadastro = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    hide = models.TextField( default=0, blank=True, null=True)  # Field name made lowercase.
    cotacaocompra_pkid_cotacao = models.IntegerField()  # Field name made lowercase.

    class Meta:
        managed = True
        unique_together = (('pkid_item', 'cotacaocompra_pkid_cotacao'),)


class Itemvenda(models.Model):
    pkid_item = models.AutoField(primary_key=True, max_length=45)  # Field name made lowercase.
    pedido_venda_idpedido_venda = models.IntegerField()
    produto = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    descricaoproduto = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    unidademedida_pkid_unidademedida = models.IntegerField()  # Field name made lowercase.
    precounitario = models.TextField(blank=True, null=True)  # Field name made lowercase.
    totalvenda = models.TextField(blank=True, null=True)  # Field name made lowercase.
    dt_cadastro = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    hide = models.TextField( default=0, blank=True, null=True)  # Field name made lowercase.
    produtos_idprodutos = models.IntegerField()  # Field name made lowercase.
    usuario_pkid_usuario = models.IntegerField()  # Field name made lowercase.

    class Meta:
        managed = True
        unique_together = (('pkid_item', 'pedido_venda_idpedido_venda'),)


class Linhavenda(models.Model):
    pkid_linhavenda = models.AutoField(primary_key=True)  # Field name made lowercase.
    pedidovenda_pkid_venda = models.IntegerField()  # Field name made lowercase.
    fkid_produto = models.IntegerField()  # Field name made lowercase.
    quantidade = models.IntegerField()  # Field name made lowercase.
    precovenda = models.TextField()  # Field name made lowercase.
    fkid_usuario_alteracao = models.IntegerField()  # Field name made lowercase.
    dt_alteracao = models.DateTimeField()  # Field name made lowercase.
    dt_cadastro = models.DateTimeField()  # Field name made lowercase.
    hide = models.TextField( default=0)  # Field name made lowercase.

    class Meta:
        managed = True
        unique_together = (('pkid_linhavenda', 'pedidovenda_pkid_venda'),)


class Materiaprima(models.Model):
    pkid_materiaprima = models.AutoField(primary_key=True)
    materiaprima = models.CharField('Matéria Prima', max_length=60)
    marca = models.CharField('Marca', max_length=50, blank=True, null=True)
    totalestoque = models.IntegerField('Qtd. em Estoque')
    unidade = models.ForeignKey('Unidademedida', on_delete=models.DO_NOTHING, verbose_name='Unidade')
    hide = models.BooleanField(default=False)

    def __str__(self):
        return self.materiaprima

    class Meta:
        managed = True
        verbose_name = 'Matéria Prima'
        verbose_name_plural = 'Matérias Primas'

class Formula_materia(models.Model):
    pkid_formula_materia = models.AutoField(primary_key=True)
    fkid_formulaproduto = models.ForeignKey(
        Formulaproduto, 
        on_delete=models.DO_NOTHING,
        verbose_name='Fórmula')
    fkid_materiaprima = models.ForeignKey(
        Materiaprima, 
        on_delete=models.DO_NOTHING,
        verbose_name='Matéria Prima')
    quantidade = models.FloatField('Quantidade')

    def __str__(self):
        return f'{self.fkid_materiaprima.materiaprima} : {self.fkid_formulaproduto.fkid_produto.nomeproduto}'

    class Meta:
        verbose_name = 'Matéria Prima : Fórmula'
        verbose_name_plural = 'Matérias Fórmulas (Relação)'


class Movimentacao(models.Model):
    pkid_movimentacao = models.AutoField(primary_key=True)  # Field name made lowercase.
    fkid_produto = models.IntegerField()  # Field name made lowercase.
    tipomovimentacao = models.TextField()  # Field name made lowercase.
    numentradas = models.IntegerField()  # Field name made lowercase.
    numsaidas = models.IntegerField()  # Field name made lowercase.
    dt_cadastro = models.DateTimeField()  # Field name made lowercase.
    dt_alteracao = models.DateTimeField()  # Field name made lowercase.
    hide = models.TextField( default=0)  # Field name made lowercase.
    fkid_linhavenda1 = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    fkid_venda = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    fkid_pedidofabri = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    fkid_estoque = models.IntegerField()  # Field name made lowercase.

    class Meta:
        managed = True


class Pedidocompra(models.Model):
    pkid_compra = models.AutoField(primary_key=True)  # Field name made lowercase.
    fornecedor = models.CharField(max_length=100, blank=True, null=True)  # Field name made lowercase.
    dt_pedido = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    dt_compra = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    dt_pagamento = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    dt_recebimento = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    cotacaocompra_pkid_cotacao = models.IntegerField()  # Field name made lowercase.
    dt_cadastro = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    hide = models.TextField( default=0, blank=True, null=True)  # Field name made lowercase.
    statuscompra_pkid_status = models.IntegerField()  # Field name made lowercase.

    class Meta:
        managed = True


class Pedidofabricacao(models.Model):
    pkid_pedidofabri = models.AutoField(primary_key=True)  # Field name made lowercase.
    fkid_produto = models.IntegerField()  # Field name made lowercase.
    fkid_usuario_alteracao = models.IntegerField()  # Field name made lowercase.
    dt_cadastro = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    hide = models.TextField( default=0, blank=True, null=True)  # Field name made lowercase.
    fkid_statusfabricacao = models.IntegerField()  # Field name made lowercase.

    class Meta:
        managed = True


class Pedidovenda(models.Model):
    pkid_venda = models.AutoField(primary_key=True)  # Field name made lowercase.
    fkid_pessoa = models.IntegerField()  # Field name made lowercase.
    fkid_usuario = models.IntegerField()  # Field name made lowercase.
    dt_pedido = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    dt_pagamento = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    dt_entrega = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    fkid_usuarioalteracao = models.IntegerField()  # Field name made lowercase.
    fkid_formapag = models.IntegerField()  # Field name made lowercase.
    fkid_entrega = models.IntegerField()  # Field name made lowercase.
    dt_cadastro = models.DateTimeField()  # Field name made lowercase.
    dt_alteracao = models.DateTimeField()  # Field name made lowercase.
    hide = models.TextField( default=0)  # Field name made lowercase.
    fkid_status = models.IntegerField()  # Field name made lowercase.

    class Meta:
        managed = True


class Pessoa(models.Model):
    pkid_pessoa = models.AutoField(primary_key=True, )  # Field name made lowercase.
    nomecompleto_razaosocial = models.CharField('Nome / Razão Social', max_length=100)  # Field name made lowercase.
    apelido_nomefantasia = models.CharField('Apelido / Nome Fantasia', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField('E-mail', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    cpf_cnpj = models.CharField('CPF / CNPJ', unique=True, max_length=19, blank=True, null=True)  # Field name made lowercase.
    rg_ie = models.CharField('RG / IE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    genero = models.CharField('Gênero', max_length=1)  # Field name made lowercase.
    dt_nascimento = models.DateField('Data de Nascimento', blank=True, null=True)  # Field name made lowercase.
    st_pessoajuridica = models.BooleanField('Pessoa Jurídica', max_length=1, default=0)  # Field name made lowercase.
    tipopessoa = models.CharField('Tipo da Pessoa', max_length=15, null=False, blank=False)
    hide = models.BooleanField(default=0)  # Field name made lowercase.

    def __str__(self):
        return self.nomecompleto_razaosocial

    class Meta:
        managed = True
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'


class Produto(models.Model):
    pkid_produto = models.AutoField(primary_key=True, )  # Field name made lowercase.
    fkid_categoria = models.ForeignKey(
        'Categoriaproduto', 
        on_delete=models.DO_NOTHING,
        verbose_name='Categoria')  # Field name made lowercase.
    fkid_unidademedida = models.ForeignKey(
        'Unidademedida', 
        on_delete=models.DO_NOTHING, 
        verbose_name='Unidade de Medida')  # Field name made lowercase.
    codproduto = models.CharField('Código', unique=True, max_length=8)  # Field name made lowercase.
    nomeproduto = models.CharField('Nome do Produto', max_length=50)  # Field name made lowercase.
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)  # Field name made lowercase. This field type is a guess.
    precocusto = models.DecimalField('Preço de Custo', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    totalestoque = models.IntegerField('Qtd. em Estoque', default=0)  # Field name made lowercase.
    descricao = models.CharField('Descrição', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sabor = models.CharField('Sabor', max_length=45, blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField('Marca', max_length=50, blank=True, null=True)  # Field name made lowercase.
    altura = models.IntegerField('Altura')  # Field name made lowercase.
    largura = models.IntegerField('Largura')  # Field name made lowercase.
    profundidade = models.IntegerField('Profundidade')  # Field name made lowercase.
    peso = models.DecimalField('Peso', max_digits=10, decimal_places=3, )  # Field name made lowercase.
    fotoproduto = models.FileField('Foto do Produto', upload_to='uploads/%Y/%m',max_length=1000, blank=True, null=True)  # Field name made lowercase.
    hide = models.BooleanField(default=0)  # Field name made lowercase.

    def __str__(self):
        return self.nomeproduto

    class Meta:
        managed = True
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
		

class Statuscompra(models.Model):
    pkid_status = models.AutoField(primary_key=True)  # Field name made lowercase.
    descricaostatus = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True


class Statusfabricacao(models.Model):
    pkid_status = models.AutoField(primary_key=True)  # Field name made lowercase.
    descricaostatus = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True


class Statusvenda(models.Model):
    pkid_status = models.AutoField(primary_key=True)  # Field name made lowercase.
    descricaostatus = models.CharField(max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True


class Telefone(models.Model):
    pkid_telefone = models.AutoField(primary_key=True)  # Field name made lowercase.
    fkid_pessoa = models.ForeignKey(
        'Pessoa', on_delete=models.DO_NOTHING, 
        verbose_name='Pessoa')  # Field name made lowercase.
    ddi = models.CharField('DDI', max_length=2, default=55)  # Field name made lowercase.
    ddd = models.CharField('DDD', max_length=2)  # Field name made lowercase.
    numero = models.CharField('Número', max_length=15)  # Field name made lowercase.
    hide = models.BooleanField(default=0)  # Field name made lowercase.

    def __str__(self):
        return f'{self.fkid_pessoa.nomecompleto_razaosocial} ({self.ddd}){self.numero}'

    class Meta:
        managed = True
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'


class Unidademedida(models.Model):
    pkid_unidademedida = models.AutoField(primary_key=True)  # Field name made lowercase.
    unidademedida = models.CharField('Unidade', max_length=50)  # Field name made lowercase.
    hide = models.BooleanField(default=0)  # Field name made lowercase.

    def __str__(self):
        return self.unidademedida

    class Meta:
        managed = True
        verbose_name = 'Unidade de Medida'
        verbose_name_plural = 'Unidades de Medida'
		

class Usuario(models.Model):
    pkid_usuario = models.AutoField(primary_key=True)  # Field name made lowercase.
    nomecompleto = models.CharField(max_length=45)  # Field name made lowercase.
    login = models.CharField(unique=True, max_length=45)  # Field name made lowercase.
    senha = models.CharField(max_length=45)  # Field name made lowercase.
    dt_importacao = models.DateTimeField()  # Field name made lowercase.
    dt_alteracao = models.DateTimeField()  # Field name made lowercase.
    hide = models.TextField( default=0)  # Field name made lowercase.

    class Meta:
        managed = True


class Usuarioalteracao(models.Model):
    pkid_usuario_alteracao = models.AutoField(primary_key=True)  # Field name made lowercase.
    dt_alteracao = models.DateTimeField()  # Field name made lowercase.
    tipo_alteracao = models.TextField()  # Field name made lowercase.

    class Meta:
        managed = True
