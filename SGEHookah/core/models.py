# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

__all__ = ["Categoriaproduto", "Produto", "Unidademedida", "Pessoa", "Endereco", "Telefone", "Telefone"]

class Categoriaproduto(models.Model):
    pkid_categoria = models.AutoField(primary_key=True)  # Field name made lowercase.
    nomecategoria = models.CharField(unique=True, max_length=100)  # Field name made lowercase.
    hide = models.BooleanField(default=0)  # Field name made lowercase.

    def __str__(self):
        return self.nomecategoria

    class Meta:
        managed = True


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
    fkid_pessoa = models.ForeignKey('Pessoa', models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    logradouro = models.CharField(max_length=100)  # Field name made lowercase.
    numero = models.CharField(max_length=7, null=True, blank=True)  # Field name made lowercase.
    complemento = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(max_length=9)  # Field name made lowercase.
    bairro = models.CharField(max_length=100)  # Field name made lowercase.
    cidade = models.CharField(max_length=150)  # Field name made lowercase.
    uf = models.CharField(max_length=2)  # Field name made lowercase.
    hide = models.BooleanField( default=0)  # Field name made lowercase.

    class Meta:
        managed = True


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
    fkid_produto = models.IntegerField()  # Field name made lowercase.
    fkid_formula_materia = models.ForeignKey('Formula_materia', models.DO_NOTHING, blank=False, null=False)  # Field name made lowercase.
    tempomaturacao = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    fkid_usuario_alteracao = models.IntegerField()  # Field name made lowercase.
    dt_cadastro = models.DateTimeField()  # Field name made lowercase.
    dt_alteracao = models.DateTimeField()  # Field name made lowercase.
    hide = models.TextField(default=0)  # Field name made lowercase.

    class Meta:
        managed = True

class Formula_materia(models.Model):
    pkid_formula_materia = models.AutoField(primary_key=True)
    fkid_formulaproduto = models.ForeignKey('Formulaproduto', models.DO_NOTHING, blank=False, null=False)
    fkid_materiaprima = models.ForeignKey('Materiaprima', models.DO_NOTHING, blank=False, null=False)

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
    pkid_materiaprima = models.AutoField(primary_key=True, )  # Field name made lowercase.
    materiaprima = models.CharField(max_length=100, blank=True, null=True)  # Field name made lowercase.
    totalestoque = models.IntegerField()  # Field name made lowercase.
    dt_cadastro = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    fkid_estoque = models.IntegerField()  # Field name made lowercase.

    class Meta:
        managed = True


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
    nomecompleto_razaosocial = models.CharField(max_length=100)  # Field name made lowercase.
    apelido_nomefantasia = models.CharField(max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    cpf_cnpj = models.CharField(unique=True, max_length=19, blank=True, null=True)  # Field name made lowercase.
    rg_ie = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    genero = models.CharField(max_length=1)  # Field name made lowercase.
    dt_nascimento = models.DateField(blank=True, null=True)  # Field name made lowercase.
    st_pessoajuridica = models.BooleanField(max_length=1, default=0)  # Field name made lowercase.
    tipopessoa = models.CharField(max_length=15, null=False, blank=False)
    hide = models.BooleanField(default=0)  # Field name made lowercase.

    class Meta:
        managed = True


class Produto(models.Model):
    pkid_produto = models.AutoField(primary_key=True, )  # Field name made lowercase.
    fkid_categoria = models.ForeignKey('Categoriaproduto', models.DO_NOTHING, )  # Field name made lowercase.
    fkid_unidademedida = models.ForeignKey('Unidademedida', models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    codproduto = models.CharField(unique=True, max_length=8)  # Field name made lowercase.
    nomeproduto = models.CharField(max_length=50)  # Field name made lowercase.
    preco = models.DecimalField(max_digits=10, decimal_places=2)  # Field name made lowercase. This field type is a guess.
    precocusto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    totalestoque = models.IntegerField(default=0)  # Field name made lowercase.
    descricao = models.CharField(max_length=300, blank=True, null=True)  # Field name made lowercase.
    sabor = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    altura = models.IntegerField()  # Field name made lowercase.
    largura = models.IntegerField()  # Field name made lowercase.
    profundidade = models.IntegerField()  # Field name made lowercase.
    peso = models.DecimalField(max_digits=10, decimal_places=3, )  # Field name made lowercase.
    fotoproduto = models.FileField(upload_to='uploads/%Y/%m',max_length=1000, blank=True, null=True)  # Field name made lowercase.
    hide = models.BooleanField(default=0)  # Field name made lowercase.

    def __str__(self):
        return self.nomeproduto

    class Meta:
        managed = True
		

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
    fkid_pessoa = models.ForeignKey('Pessoa', models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    ddi = models.CharField(max_length=2, default=55)  # Field name made lowercase.
    ddd = models.CharField(max_length=2)  # Field name made lowercase.
    numero = models.CharField(max_length=15)  # Field name made lowercase.
    hide = models.TextField( default=0)  # Field name made lowercase.

    class Meta:
        managed = True


class Unidademedida(models.Model):
    pkid_unidademedida = models.AutoField(primary_key=True)  # Field name made lowercase.
    unidademedida = models.CharField(unique=True, max_length=50)  # Field name made lowercase.
    hide = models.BooleanField( default=0)  # Field name made lowercase.

    def __str__(self):
        return self.unidademedida

    class Meta:
        managed = True
		

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
