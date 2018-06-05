# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

__all__ = ["Categoriaproduto", "Produto", "AuthUser", "Unidademedida", "Pessoa", "Endereco", "Telefone", "Tipopessoa"]

class Categoriaproduto(models.Model):
		pkid_categoria = models.IntegerField(primary_key=True, db_column='PKID_Categoria')  # Field name made lowercase.
		nomecategoria = models.CharField(db_column='NomeCategoria', unique=True, max_length=100)  # Field name made lowercase.
		hide = models.BooleanField(db_column='HIDE')  # Field name made lowercase.

		def __str__(self):
			return self.nomecategoria

		class Meta:
				managed = True
				db_table = 'CategoriaProduto'


class Cotacaocompra(models.Model):
    pkid_cotacao = models.IntegerField(db_column='PKID_Cotacao', primary_key=True)  # Field name made lowercase.
    fornecedor = models.CharField(db_column='Fornecedor', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dt_cotacao = models.DateTimeField(db_column='DT_Cotacao', blank=True, null=True)  # Field name made lowercase.
    dt_entrega = models.DateTimeField(db_column='DT_entrega', blank=True, null=True)  # Field name made lowercase.
    formapamento = models.CharField(db_column='FormaPamento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pedidocompra_pkid_compra = models.IntegerField(db_column='PedidoCompra_PKID_Compra')  # Field name made lowercase.
    statuscotacao_pkid_status = models.IntegerField(db_column='StatusCotacao_PKID_Status')  # Field name made lowercase.
    dt_cadastro = models.DateTimeField(db_column='DT_Cadastro', blank=True, null=True)  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(db_column='DT_Alteracao', blank=True, null=True)  # Field name made lowercase.
    hide = models.TextField(db_column='HIDE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'CotacaoCompra'


class Endereco(models.Model):
    pkid_endereco = models.IntegerField(db_column='PKID_Endereco')  # Field name made lowercase.
    logradouro = models.CharField(db_column='Logradouro', max_length=100)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=7)  # Field name made lowercase.
    complemento = models.CharField(db_column='Complemento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=9)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=100)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=150)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2)  # Field name made lowercase.
    hide = models.BooleanField(db_column='HIDE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Endereco'


class Entrega(models.Model):
    pkid_entrega = models.IntegerField(db_column='PKID_Entrega', primary_key=True)  # Field name made lowercase.
    dataentrega = models.DateTimeField(db_column='DataEntrega', blank=True, null=True)  # Field name made lowercase.
    formaentrega = models.CharField(db_column='FormaEntrega', max_length=100, blank=True, null=True)  # Field name made lowercase.
    valorfrete = models.TextField(db_column='ValorFrete', blank=True, null=True)  # Field name made lowercase.
    nomecontarecebimento = models.CharField(db_column='NomeContaRecebimento', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fkid_usuario_alteracao = models.IntegerField(db_column='FKID_Usuario_Alteracao')  # Field name made lowercase.
    dt_cadastro = models.DateTimeField(db_column='DT_Cadastro')  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(db_column='DT_Alteracao')  # Field name made lowercase.
    hide = models.TextField(db_column='HIDE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Entrega'


class Formapagamento(models.Model):
    pkid_formapag = models.IntegerField(db_column='PKID_FormaPag', primary_key=True)  # Field name made lowercase.
    formapagamento = models.CharField(db_column='FormaPagamento', max_length=50)  # Field name made lowercase.
    fkid_usuario_alteracao = models.IntegerField(db_column='FKID_Usuario_Alteracao')  # Field name made lowercase.
    dt_cadastro = models.DateTimeField(db_column='DT_Cadastro')  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(db_column='DT_Alteracao')  # Field name made lowercase.
    hide = models.TextField(db_column='HIDE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'FormaPagamento'


class Formulaproduto(models.Model):
    pkid_formula = models.IntegerField(db_column='PKID_Formula', primary_key=True)  # Field name made lowercase.
    fkid_produto = models.IntegerField(db_column='FKID_Produto')  # Field name made lowercase.
    fkid_materiaprima = models.IntegerField(db_column='FKID_MateriaPrima')  # Field name made lowercase.
    tempomatucao = models.IntegerField(db_column='TempoMatucao', blank=True, null=True)  # Field name made lowercase.
    fkid_usuario_alteracao = models.IntegerField(db_column='FKID_Usuario_Alteracao')  # Field name made lowercase.
    dt_cadastro = models.DateTimeField(db_column='DT_Cadastro')  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(db_column='DT_Alteracao')  # Field name made lowercase.
    hide = models.TextField(db_column='HIDE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'FormulaProduto'


class Itemcompra(models.Model):
    pkid_item = models.IntegerField(db_column='PKID_Item', primary_key=True)  # Field name made lowercase.
    produto = models.CharField(db_column='Produto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descricaoproduto = models.CharField(db_column='DescricaoProduto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.IntegerField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    precounitario = models.TextField(db_column='PrecoUnitario', blank=True, null=True)  # Field name made lowercase.
    totalvenda = models.TextField(db_column='TotalVenda', blank=True, null=True)  # Field name made lowercase.
    dt_cadastro = models.DateTimeField(db_column='DT_Cadastro', blank=True, null=True)  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(db_column='DT_Alteracao', blank=True, null=True)  # Field name made lowercase.
    hide = models.TextField(db_column='HIDE', blank=True, null=True)  # Field name made lowercase.
    pedidocompra_pkid_compra = models.IntegerField(db_column='PedidoCompra_PKID_Compra')  # Field name made lowercase.
    statuscompra_pkid_status = models.IntegerField(db_column='StatusCompra_PKID_Status')  # Field name made lowercase.
    unidademedidacompra_pkid_unidademedida = models.IntegerField(db_column='UnidadeMedidaCompra_PKID_UnidadeMedida')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ItemCompra'
        unique_together = (('pkid_item', 'pedidocompra_pkid_compra'),)


class Itemcotacao(models.Model):
    pkid_item = models.IntegerField(db_column='PKID_Item', primary_key=True)  # Field name made lowercase.
    produto = models.CharField(db_column='Produto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descricaoproduto = models.CharField(db_column='DescricaoProduto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.IntegerField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    precounitario = models.TextField(db_column='PrecoUnitario', blank=True, null=True)  # Field name made lowercase.
    totalvenda = models.TextField(db_column='TotalVenda', blank=True, null=True)  # Field name made lowercase.
    dt_cadastro = models.DateTimeField(db_column='DT_Cadastro', blank=True, null=True)  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(db_column='DT_Alteracao', blank=True, null=True)  # Field name made lowercase.
    hide = models.TextField(db_column='HIDE', blank=True, null=True)  # Field name made lowercase.
    cotacaocompra_pkid_cotacao = models.IntegerField(db_column='CotacaoCompra_PKID_Cotacao')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ItemCotacao'
        unique_together = (('pkid_item', 'cotacaocompra_pkid_cotacao'),)


class Itemvenda(models.Model):
    pkid_item = models.CharField(db_column='PKID_Item', primary_key=True, max_length=45)  # Field name made lowercase.
    pedido_venda_idpedido_venda = models.IntegerField()
    produto = models.CharField(db_column='Produto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descricaoproduto = models.CharField(db_column='DescricaoProduto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.IntegerField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    unidademedida_pkid_unidademedida = models.IntegerField(db_column='UnidadeMedida_PKID_UnidadeMedida')  # Field name made lowercase.
    precounitario = models.TextField(db_column='PrecoUnitario', blank=True, null=True)  # Field name made lowercase.
    totalvenda = models.TextField(db_column='TotalVenda', blank=True, null=True)  # Field name made lowercase.
    dt_cadastro = models.DateTimeField(db_column='DT_Cadastro', blank=True, null=True)  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(db_column='DT_Alteracao', blank=True, null=True)  # Field name made lowercase.
    hide = models.TextField(db_column='HIDE', blank=True, null=True)  # Field name made lowercase.
    produtos_idprodutos = models.IntegerField(db_column='Produtos_idProdutos')  # Field name made lowercase.
    usuario_pkid_usuario = models.IntegerField(db_column='Usuario_PKID_Usuario')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ItemVenda'
        unique_together = (('pkid_item', 'pedido_venda_idpedido_venda'),)


class Linhavenda(models.Model):
    pkid_linhavenda = models.IntegerField(db_column='PKID_LinhaVenda', primary_key=True)  # Field name made lowercase.
    pedidovenda_pkid_venda = models.IntegerField(db_column='PedidoVenda_PKID_Venda')  # Field name made lowercase.
    fkid_produto = models.IntegerField(db_column='FKID_Produto')  # Field name made lowercase.
    quantidade = models.IntegerField(db_column='Quantidade')  # Field name made lowercase.
    precovenda = models.TextField(db_column='PrecoVenda')  # Field name made lowercase.
    fkid_usuario_alteracao = models.IntegerField(db_column='FKID_Usuario_Alteracao')  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(db_column='DT_Alteracao')  # Field name made lowercase.
    dt_cadastro = models.DateTimeField(db_column='DT_Cadastro')  # Field name made lowercase.
    hide = models.TextField(db_column='HIDE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LinhaVenda'
        unique_together = (('pkid_linhavenda', 'pedidovenda_pkid_venda'),)


class Materiaprima(models.Model):
    pkid_materiaprima = models.IntegerField(primary_key=True, db_column='PKID_MateriaPrima')  # Field name made lowercase.
    materiaprima = models.CharField(db_column='MateriaPrima', max_length=100, blank=True, null=True)  # Field name made lowercase.
    totalestoque = models.IntegerField(db_column='TotalEstoque')  # Field name made lowercase.
    dt_cadastro = models.DateTimeField(db_column='DT_Cadastro', blank=True, null=True)  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(db_column='DT_Alteracao', blank=True, null=True)  # Field name made lowercase.
    fkid_estoque = models.IntegerField(db_column='FKID_Estoque')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'MateriaPrima'


class Movimentacao(models.Model):
    pkid_movimentacao = models.IntegerField(db_column='PKID_Movimentacao', primary_key=True)  # Field name made lowercase.
    fkid_produto = models.IntegerField(db_column='FKID_Produto')  # Field name made lowercase.
    tipomovimentacao = models.TextField(db_column='TipoMovimentacao')  # Field name made lowercase.
    numentradas = models.IntegerField(db_column='NumEntradas')  # Field name made lowercase.
    numsaidas = models.IntegerField(db_column='NumSaidas')  # Field name made lowercase.
    dt_cadastro = models.DateTimeField(db_column='DT_Cadastro')  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(db_column='DT_Alteracao')  # Field name made lowercase.
    hide = models.TextField(db_column='HIDE')  # Field name made lowercase.
    fkid_linhavenda1 = models.IntegerField(db_column='FKID_LinhaVenda1', blank=True, null=True)  # Field name made lowercase.
    fkid_venda = models.IntegerField(db_column='FKID_Venda', blank=True, null=True)  # Field name made lowercase.
    fkid_pedidofabri = models.IntegerField(db_column='FKID_PedidoFabri', blank=True, null=True)  # Field name made lowercase.
    fkid_estoque = models.IntegerField(db_column='FKID_Estoque')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Movimentacao'


class Pedidocompra(models.Model):
    pkid_compra = models.IntegerField(db_column='PKID_Compra', primary_key=True)  # Field name made lowercase.
    fornecedor = models.CharField(db_column='Fornecedor', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dt_pedido = models.DateTimeField(db_column='DT_Pedido', blank=True, null=True)  # Field name made lowercase.
    dt_compra = models.DateTimeField(db_column='DT_Compra', blank=True, null=True)  # Field name made lowercase.
    dt_pagamento = models.DateTimeField(db_column='DT_Pagamento', blank=True, null=True)  # Field name made lowercase.
    dt_recebimento = models.DateTimeField(db_column='DT_Recebimento', blank=True, null=True)  # Field name made lowercase.
    cotacaocompra_pkid_cotacao = models.IntegerField(db_column='CotacaoCompra_PKID_Cotacao')  # Field name made lowercase.
    dt_cadastro = models.DateTimeField(db_column='DT_Cadastro', blank=True, null=True)  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(db_column='DT_Alteracao', blank=True, null=True)  # Field name made lowercase.
    hide = models.TextField(db_column='HIDE', blank=True, null=True)  # Field name made lowercase.
    statuscompra_pkid_status = models.IntegerField(db_column='StatusCompra_PKID_Status')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PedidoCompra'


class Pedidofabricacao(models.Model):
    pkid_pedidofabri = models.IntegerField(db_column='PKID_PedidoFabri', primary_key=True)  # Field name made lowercase.
    fkid_produto = models.IntegerField(db_column='FKID_Produto')  # Field name made lowercase.
    fkid_usuario_alteracao = models.IntegerField(db_column='FKID_Usuario_Alteracao')  # Field name made lowercase.
    dt_cadastro = models.DateTimeField(db_column='DT_Cadastro', blank=True, null=True)  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(db_column='DT_Alteracao', blank=True, null=True)  # Field name made lowercase.
    hide = models.TextField(db_column='HIDE', blank=True, null=True)  # Field name made lowercase.
    fkid_statusfabricacao = models.IntegerField(db_column='FKID_StatusFabricacao')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PedidoFabricacao'


class Pedidovenda(models.Model):
    pkid_venda = models.IntegerField(db_column='PKID_Venda', primary_key=True)  # Field name made lowercase.
    fkid_pessoa = models.IntegerField(db_column='FKID_Pessoa')  # Field name made lowercase.
    fkid_usuario = models.IntegerField(db_column='FKID_Usuario')  # Field name made lowercase.
    dt_pedido = models.DateTimeField(db_column='DT_Pedido', blank=True, null=True)  # Field name made lowercase.
    dt_pagamento = models.DateTimeField(db_column='DT_Pagamento', blank=True, null=True)  # Field name made lowercase.
    dt_entrega = models.DateTimeField(db_column='DT_Entrega', blank=True, null=True)  # Field name made lowercase.
    fkid_usuarioalteracao = models.IntegerField(db_column='FKID_UsuarioAlteracao')  # Field name made lowercase.
    fkid_formapag = models.IntegerField(db_column='FKID_FormaPag')  # Field name made lowercase.
    fkid_entrega = models.IntegerField(db_column='FKID_Entrega')  # Field name made lowercase.
    dt_cadastro = models.DateTimeField(db_column='DT_Cadastro')  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(db_column='DT_Alteracao')  # Field name made lowercase.
    hide = models.TextField(db_column='HIDE')  # Field name made lowercase.
    fkid_status = models.IntegerField(db_column='FKID_Status')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PedidoVenda'


class Pessoa(models.Model):
    pkid_pessoa = models.IntegerField(primary_key=True, db_column='PKID_Pessoa')  # Field name made lowercase.
    nomecompleto_razaosocial = models.CharField(db_column='NomeCompleto_RazaoSocial', max_length=100)  # Field name made lowercase.
    apelido_nomefantasia = models.CharField(db_column='Apelido_NomeFantasia', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    cpf_cnpj = models.CharField(db_column='CPF_CNPJ', unique=True, max_length=19, blank=True, null=True)  # Field name made lowercase.
    rg_ie = models.CharField(db_column='RG_IE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    genero = models.CharField(db_column='Genero', max_length=1)  # Field name made lowercase.
    dt_nascimento = models.DateField(db_column='DT_Nascimento', blank=True, null=True)  # Field name made lowercase.
    st_pessoajuridica = models.CharField(db_column='ST_PessoaJuridica', max_length=1)  # Field name made lowercase.
    fkid_endereco = models.IntegerField(db_column='FKID_Endereco', blank=True, null=True)  # Field name made lowercase.
    fkid_tipopessoa = models.ForeignKey('Tipopessoa', models.DO_NOTHING, db_column='FKID_TipoPessoa')  # Field name made lowercase.
    hide = models.BooleanField(db_column='HIDE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Pessoa'


class Produto(models.Model):
		pkid_produto = models.IntegerField(primary_key=True, db_column='PKID_Produto')  # Field name made lowercase.
		fkid_categoria = models.ForeignKey(Categoriaproduto, models.DO_NOTHING, db_column='FKID_Categoria')  # Field name made lowercase.
		fkid_unidademedida = models.ForeignKey('Unidademedida', models.DO_NOTHING, db_column='FKID_UnidadeMedida', blank=True, null=True)  # Field name made lowercase.
		codproduto = models.CharField(db_column='CodProduto', unique=True, max_length=8)  # Field name made lowercase.
		nomeproduto = models.CharField(db_column='NomeProduto', max_length=50)  # Field name made lowercase.
		preco = models.DecimalField(db_column='Preco', max_digits=10, decimal_places=2)  # Field name made lowercase. This field type is a guess.
		precocusto = models.DecimalField(db_column='PrecoCusto', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
		totalestoque = models.IntegerField(db_column='TotalEstoque')  # Field name made lowercase.
		descricao = models.CharField(db_column='Descricao', max_length=300, blank=True, null=True)  # Field name made lowercase.
		sabor = models.CharField(db_column='Sabor', max_length=45, blank=True, null=True)  # Field name made lowercase.
		marca = models.CharField(db_column='Marca', max_length=50, blank=True, null=True)  # Field name made lowercase.
		altura = models.IntegerField(db_column='Altura')  # Field name made lowercase.
		largura = models.IntegerField(db_column='Largura')  # Field name made lowercase.
		profundidade = models.IntegerField(db_column='Profundidade')  # Field name made lowercase.
		peso = models.DecimalField(max_digits=10, decimal_places=3, db_column='Peso')  # Field name made lowercase.
		fotoproduto = models.FileField(upload_to='uploads/%Y/%m',db_column='FotoProduto', max_length=1000, blank=True, null=True)  # Field name made lowercase.
		hide = models.BooleanField(db_column='HIDE')  # Field name made lowercase.

		def __str__(self):
			return self.nomeproduto

		class Meta:
				managed = True
				db_table = 'Produto'


class Statuscompra(models.Model):
    pkid_status = models.IntegerField(db_column='PKID_Status', primary_key=True)  # Field name made lowercase.
    descricaostatus = models.CharField(db_column='DescricaoStatus', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'StatusCompra'


class Statusfabricacao(models.Model):
    pkid_status = models.IntegerField(db_column='PKID_Status', primary_key=True)  # Field name made lowercase.
    descricaostatus = models.CharField(db_column='DescricaoStatus', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'StatusFabricacao'


class Statusvenda(models.Model):
    pkid_status = models.IntegerField(db_column='PKID_Status', primary_key=True)  # Field name made lowercase.
    descricaostatus = models.CharField(db_column='DescricaoStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'StatusVenda'


class Telefone(models.Model):
    pkid_telefone = models.IntegerField(db_column='PKID_Telefone', primary_key=True)  # Field name made lowercase.
    fkid_pessoa = models.ForeignKey('Pessoa', models.DO_NOTHING, db_column='FKID_Pessoa', blank=True, null=True)  # Field name made lowercase.
    ddi = models.IntegerField(db_column='DDI')  # Field name made lowercase.
    ddd = models.IntegerField(db_column='DDD')  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero')  # Field name made lowercase.
    hide = models.TextField(db_column='HIDE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Telefone'


class Tipopessoa(models.Model):
    pkid_tipopessoa = models.IntegerField(primary_key=True, db_column='PKID_TipoPessoa')  # Field name made lowercase.
    tipopessoa = models.CharField(db_column='TipoPessoa', unique=True, max_length=100)  # Field name made lowercase.
    hide = models.BooleanField(db_column='HIDE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TipoPessoa'


class Unidademedida(models.Model):
		pkid_unidademedida = models.IntegerField(primary_key=True, db_column='PKID_UnidadeMedida')  # Field name made lowercase.
		unidademedida = models.CharField(db_column='UnidadeMedida', unique=True, max_length=50)  # Field name made lowercase.
		hide = models.BooleanField(db_column='HIDE')  # Field name made lowercase.

		def __str__(self):
			return self.unidademedida

		class Meta:
				managed = True
				db_table = 'UnidadeMedida'


class Usuario(models.Model):
    pkid_usuario = models.IntegerField(db_column='PKID_Usuario', primary_key=True)  # Field name made lowercase.
    nomecompleto = models.CharField(db_column='NomeCompleto', max_length=45)  # Field name made lowercase.
    login = models.CharField(db_column='Login', unique=True, max_length=45)  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=45)  # Field name made lowercase.
    dt_importacao = models.DateTimeField(db_column='DT_Importacao')  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(db_column='DT_Alteracao')  # Field name made lowercase.
    hide = models.TextField(db_column='HIDE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Usuario'


class Usuarioalteracao(models.Model):
    pkid_usuario_alteracao = models.IntegerField(db_column='PKID_Usuario_Alteracao', primary_key=True)  # Field name made lowercase.
    dt_alteracao = models.DateTimeField(db_column='DT_Alteracao')  # Field name made lowercase.
    tipo_alteracao = models.TextField(db_column='Tipo_Alteracao')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'UsuarioAlteracao'
				
class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'