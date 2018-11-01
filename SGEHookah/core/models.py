"""
    Modelos do banco de dados
"""

import datetime as dt

from django.db import models
from django.contrib.auth.models import User

class Categoriaproduto(models.Model):
    """ Categoria de produto """
    pkid_categoria = models.AutoField(primary_key=True)
    nomecategoria = models.CharField(
        'Nome da Categoria', unique=True, max_length=100)
    hide = models.BooleanField(default=0)

    def __str__(self):
        return self.nomecategoria

    class Meta:
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias (Produto)'


class Cotacaocompra(models.Model):
    """ Cotacação de compras """
    pkid_cotacao = models.AutoField(primary_key=True)
    fornecedor = models.CharField(max_length=100, blank=True, null=True)
    dt_cotacao = models.DateTimeField(blank=True, null=True)
    dt_entrega = models.DateTimeField(blank=True, null=True)
    formapamento = models.CharField(max_length=45, blank=True, null=True)
    pedidocompra_pkid_compra = models.IntegerField()
    statuscotacao_pkid_status = models.IntegerField()
    dt_cadastro = models.DateTimeField(blank=True, null=True)
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    hide = models.BooleanField(default=0)

    class Meta:
        managed = True


class Endereco(models.Model):
    """ Armazena informações sobre um Endereço """
    pkid_endereco = models.AutoField(primary_key=True)
    fkid_pessoa = models.ForeignKey(
        'Pessoa', models.CASCADE,
        blank=True, null=True,
        verbose_name='Pessoa')
    logradouro = models.CharField('Endereço', max_length=100)
    endereco_numero = models.CharField('Número', max_length=7, null=True, blank=True)
    complemento = models.CharField(
        'Complemento', max_length=45, blank=True, null=True)
    cep = models.CharField('CEP', max_length=9)
    bairro = models.CharField('Bairro', max_length=100)
    cidade = models.CharField('Cidade', max_length=150)
    uf = models.CharField('Estado', max_length=2)
    hide = models.BooleanField(default=0)

    def __str__(self):
        return f'{self.fkid_pessoa.nomecompleto_razaosocial} : {self.cep}'

    class Meta:
        managed = True
        verbose_name = 'Endereço (Pessoa : CEP)'
        verbose_name_plural = 'Endereços'

class TipoEntrega(models.Model):
    pkid_tipoentrega = models.AutoField(primary_key=True)
    descricao = models.CharField('TipoEntrega', max_length=30)

class Entrega(models.Model):
    """ Armazena informações sobre alguma entrega """
    pkid_entrega = models.AutoField(primary_key=True)
    fkid_tipoentrega = models.ForeignKey("TipoEntrega", on_delete=models.CASCADE)
    fkid_venda = models.ForeignKey("PedidoVenda", on_delete=models.CASCADE)
    dataentrega = models.DateTimeField(blank=True, null=True)
    valorfrete = models.TextField(blank=True, null=True)
    hide = models.BooleanField(default=0)

    def __str__(self):
        return self.formaentrega

    class Meta:
        managed = True
        verbose_name = 'Forma de Entrega'
        verbose_name_plural = 'Formas de Entrega'


class Formapagamento(models.Model):
    """ Armazena informações sobre formas de pagamento """
    pkid_formapag = models.AutoField(primary_key=True)
    formapagamento = models.CharField(max_length=50)
    hide = models.BooleanField(default=0)

    def __str__(self):
        return self.formapagamento

    class Meta:
        managed = True
        verbose_name = 'Forma de Pagamento'
        verbose_name_plural = 'Formas de Pagamento'


class Formulaproduto(models.Model):
    """
        Armazena informações sobre a fórmula de um produto
        Utiliza o modelo Formulamateria como linhas de matérias
        primas necessárias
    """
    pkid_formula = models.AutoField(primary_key=True)
    fkid_produto = models.OneToOneField(
        'Produto', on_delete=models.CASCADE,
        unique=True,
        verbose_name='Produto')
    tempomaturacao = models.TimeField('Tempo de Maturação')
    hide = models.BooleanField(default=0)

    def __str__(self):
        return f'Fórmula {self.fkid_produto.nomeproduto}'

    class Meta:
        managed = True
        verbose_name = 'Fórmula Produto'
        verbose_name_plural = 'Fórmulas (Produto)'


class Itemcompra(models.Model):
    """ Linha de compra """
    pkid_item = models.AutoField(primary_key=True)
    produto = models.CharField(max_length=45, blank=True, null=True)
    descricaoproduto = models.CharField(max_length=45, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    precounitario = models.TextField(blank=True, null=True)
    totalvenda = models.TextField(blank=True, null=True)
    dt_cadastro = models.DateTimeField(blank=True, null=True)
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    hide = models.BooleanField(default=0)
    pedidocompra_pkid_compra = models.IntegerField()
    statuscompra_pkid_status = models.IntegerField()
    unidademedidacompra_pkid_unidademedida = models.IntegerField()

    class Meta:
        managed = True
        unique_together = (('pkid_item', 'pedidocompra_pkid_compra'),)


class Itemcotacao(models.Model):
    """ Item de cotação """
    pkid_item = models.AutoField(primary_key=True)
    produto = models.CharField(max_length=45, blank=True, null=True)
    descricaoproduto = models.CharField(max_length=100, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    precounitario = models.TextField(blank=True, null=True)
    totalvenda = models.TextField(blank=True, null=True)
    dt_cadastro = models.DateTimeField(blank=True, null=True)
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    hide = models.BooleanField(default=0)
    cotacaocompra_pkid_cotacao = models.IntegerField()

    class Meta:
        managed = True
        unique_together = (('pkid_item', 'cotacaocompra_pkid_cotacao'),)


class Itemvenda(models.Model):
    """ Item de venda """
    pkid_itemvenda = models.AutoField(primary_key=True)
    fkid_pedidovenda = models.ForeignKey('Pedidovenda', on_delete=models.CASCADE)
    fkid_produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    quantidade = models.IntegerField(blank=True, null=True)
    vl_total = models.DecimalField(decimal_places=2, max_digits=10)
    vl_unitario = models.DecimalField(decimal_places=2, max_digits=10)
    hide = models.BooleanField(default=0)

    def preco_unitario(self):
        produto = Produto.objects.get(pkid_produto=self.fkid_produto)
        return produto.preco

    class Meta:
        managed = True
        unique_together = (('pkid_itemvenda', 'fkid_pedidovenda'),)


class Materiaprima(models.Model):
    """ Armazena informações sobre matérias primas """
    pkid_materiaprima = models.AutoField(primary_key=True)
    materiaprima = models.CharField('Matéria Prima', max_length=60)
    marca = models.CharField('Marca', max_length=50, blank=True, null=True)
    totalestoque = models.IntegerField('Qtd. em Estoque')
    unidade = models.ForeignKey(
        'Unidademedida', on_delete=models.CASCADE, verbose_name='Unidade')
    hide = models.BooleanField(default=False)

    def __str__(self):
        return self.materiaprima

    class Meta:
        managed = True
        verbose_name = 'Matéria Prima'
        verbose_name_plural = 'Matérias Primas'


class Formulamateria(models.Model):
    """
        Modelo auxilar do Formulaproduto
        Armazena informações sobre as matérias primas
        utilizadas em um fórmula (ManyToOne)
    """
    pkid_formula_materia = models.AutoField(primary_key=True)
    fkid_formulaproduto = models.ForeignKey(
        "Formulaproduto",
        on_delete=models.CASCADE,
        verbose_name='Fórmula')
    fkid_materiaprima = models.ForeignKey(
        "Materiaprima",
        on_delete=models.CASCADE,
        verbose_name='Matéria Prima')
    quantidade = models.FloatField('Quantidade')
    unidade = models.ForeignKey(
        "Unidademedida",
        on_delete=models.CASCADE,
        verbose_name='Unidade')

    def __str__(self):
        return f'{self.fkid_materiaprima.materiaprima} : {self.fkid_formulaproduto}'

    class Meta:
        verbose_name = 'Matéria Prima : Fórmula'
        verbose_name_plural = 'Matérias Fórmulas (Relação)'


class Movimentacao(models.Model):
    """ Movimentação em estoque de algum produto """
    pkid_movimentacao = models.AutoField(primary_key=True)
    fkid_produto = models.IntegerField()
    tipomovimentacao = models.TextField()
    numentradas = models.IntegerField()
    numsaidas = models.IntegerField()
    dt_cadastro = models.DateTimeField()
    dt_alteracao = models.DateTimeField()
    hide = models.BooleanField(default=0)
    fkid_linhavenda1 = models.IntegerField(blank=True, null=True)
    fkid_venda = models.IntegerField(blank=True, null=True)
    fkid_pedidofabri = models.IntegerField(blank=True, null=True)
    fkid_estoque = models.IntegerField()

    class Meta:
        managed = True


class Pedidocompra(models.Model):
    """ Pedido compra """

    pkid_compra = models.AutoField(primary_key=True)
    fornecedor = models.CharField(max_length=100, blank=True, null=True)
    dt_pedido = models.DateTimeField(blank=True, null=True)
    dt_compra = models.DateTimeField(blank=True, null=True)
    dt_pagamento = models.DateTimeField(blank=True, null=True)
    dt_recebimento = models.DateTimeField(blank=True, null=True)
    cotacaocompra_pkid_cotacao = models.IntegerField()
    dt_cadastro = models.DateTimeField(blank=True, null=True)
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    hide = models.BooleanField(default=0)
    statuscompra_pkid_status = models.IntegerField()

    class Meta:
        managed = True


class Pedidofabricacao(models.Model):
    """ Armazena informações sobre um novo pedido de fabricação """

    pkid_pedidofabricacao = models.AutoField(primary_key=True)
    lote = models.CharField(max_length=8, blank=True, null=True, unique=True)
    fkid_formula = models.ForeignKey(
        "Formulaproduto", on_delete=models.CASCADE)
    fkid_statusfabricacao = models.ForeignKey(
        "Statusfabricacao", on_delete=models.CASCADE)
    quantidade = models.IntegerField("Quantidade")
    dt_fim_maturacao = models.DateTimeField()
    hide = models.BooleanField(default=0)

    def remover_estoque(self):
        for materia_formula, id_materia in self.materias():
            materiaprima = Materiaprima.objects.get(pkid_materiaprima=id_materia)
            materiaprima.totalestoque -= (materia_formula['quantidade'] * self.quantidade)
            materiaprima.save()
        return self

    def voltar_estoque(self):
        for materia_formula, id_materia in self.materias():
            materiaprima = Materiaprima.objects.get(pkid_materiaprima=id_materia)
            materiaprima.totalestoque += (materia_formula['quantidade'] * self.quantidade)
            materiaprima.save()
        return self

    def is_ready(self):
        """
            Checa se o pedido já pode ser retirado da maturação
        """

        return dt.datetime.now(dt.timezone.utc) >= self.dt_fim_maturacao

    def avancar_etapa(self):
        """ Avança para a próxima etapa """
        order = self.fkid_statusfabricacao.order + 1
        try:
            self.fkid_statusfabricacao = Statusfabricacao.objects.get(order=order)
            self.save()
        except:
            pass

    def product(self):
        """ Devolve o produto a ser fabricado """
        return self.fkid_formula.fkid_produto.nomeproduto

    def status_string(self):
        """ Devolve o nome do status atual do Pedido """
        return self.fkid_statusfabricacao.status

    def materias(self):
        """
            Devolve uma lista com as matérias primas necessárias
            para uma fabricação
        """

        lista = []
        materias = Formulamateria.objects.filter(
            fkid_formulaproduto=self.fkid_formula).values()
        for materia in materias:

            id_materia = materia['fkid_materiaprima_id']
            unidade = materia['unidade_id']

            materia['fkid_materiaprima_id'] = Materiaprima.objects.get(
                pkid_materiaprima=id_materia
            ).materiaprima

            materia['unidade_id'] = Unidademedida.objects.get(
                pkid_unidademedida=unidade
            ).unidademedida

            lista.append((materia, id_materia))
        return lista

    def name(self):
        """ Retorna um nome para o pedido """
        return f'Pedido nº{self.pkid_pedidofabricacao}'

    def __str__(self):
        return f'Pedido nº{self.pkid_pedidofabricacao}'

    class Meta:
        verbose_name = 'Pedido de Fabricação'
        verbose_name_plural = 'Pedidos de Fabricação'


class Pedidovenda(models.Model):
    """ Pedido de venda """
    pkid_venda = models.AutoField(primary_key=True)
    fkid_cliente = models.ForeignKey('Pessoa', on_delete=models.CASCADE, null=True)
    fkid_formapag = models.ForeignKey('Formapagamento', on_delete=models.DO_NOTHING, null=True)
    fkid_status = models.ForeignKey('Statusvenda', on_delete=models.DO_NOTHING)
    fkid_usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dt_pedido = models.DateTimeField(blank=True, null=True)
    dt_pagamento = models.DateTimeField(blank=True, null=True)
    dt_preventrega = models.DateTimeField(blank=True, null=True)
    pago = models.BooleanField(default=0)
    hide = models.BooleanField(default=0)

    def __str__(self):
        return f'Pedido nº{self.pkid_venda}'

    class Meta:
        managed = True
        verbose_name = 'Pedido de Venda'
        verbose_name_plural = 'Pedidos de Venda'


class Pessoa(models.Model):
    """
        Armazena informações sobre um cliente, fornecedor ou qualquer
        pessoa que seja preciso registrar no sistema
    """
    pkid_pessoa = models.AutoField(primary_key=True, )
    nomecompleto_razaosocial = models.CharField(
        'Nome / Razão Social', max_length=100)
    apelido_nomefantasia = models.CharField(
        'Apelido / Nome Fantasia', max_length=100, blank=True, null=True)
    email = models.CharField('E-mail', unique=True,
                             max_length=100, blank=True, null=True)
    cpf_cnpj = models.CharField(
        'CPF / CNPJ', unique=True, max_length=19, blank=True, null=True)
    rg_ie = models.CharField('RG / IE', max_length=50, blank=True, null=True)
    genero = models.CharField('Gênero', max_length=1)
    dt_nascimento = models.DateField(
        'Data de Nascimento', blank=True, null=True)
    st_pessoajuridica = models.BooleanField(
        'Pessoa Jurídica', max_length=1, default=0)
    tipopessoa = models.CharField(
        'Tipo da Pessoa', max_length=15, null=False, blank=False)
    hide = models.BooleanField(default=0)

    def __str__(self):
        return self.nomecompleto_razaosocial

    class Meta:
        managed = True
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'


class Produto(models.Model):
    """ Armazena informações sobre um produto """
    pkid_produto = models.AutoField(primary_key=True, )
    fkid_categoria = models.ForeignKey(
        'Categoriaproduto',
        on_delete=models.CASCADE,
        verbose_name='Categoria')
    fkid_unidademedida = models.ForeignKey(
        'Unidademedida',
        on_delete=models.CASCADE,
        verbose_name='Unidade de Medida')
    codproduto = models.CharField('Código', unique=True, max_length=8)
    nomeproduto = models.CharField('Nome do Produto', max_length=50)
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    precocusto = models.DecimalField(
        'Preço de Custo', max_digits=10, decimal_places=2, blank=True, null=True)
    totalestoque = models.IntegerField('Qtd. em Estoque', default=0)
    descricao = models.CharField(
        'Descrição', max_length=300, blank=True, null=True)
    sabor = models.CharField('Sabor', max_length=45, blank=True, null=True)
    marca = models.CharField('Marca', max_length=50, blank=True, null=True)
    altura = models.IntegerField('Altura')
    largura = models.IntegerField('Largura')
    profundidade = models.IntegerField('Profundidade')
    peso = models.DecimalField('Peso', max_digits=10, decimal_places=3, )
    fotoproduto = models.FileField(
        'Foto do Produto', upload_to='uploads/%Y/%m', max_length=1000, blank=True, null=True)
    vendivel = models.BooleanField(default=1)
    hide = models.BooleanField(default=0)

    def __str__(self):
        return self.nomeproduto

    class Meta:
        managed = True
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


class Statuscompra(models.Model):
    """ Status de uma compra """

    pkid_status = models.AutoField(primary_key=True)
    descricaostatus = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True


class Statusfabricacao(models.Model):
    """ Armazena as etapas (status) de pedidos de fabricação"""

    pkid_status = models.AutoField(primary_key=True)
    order = models.IntegerField("Ordem")
    status = models.CharField("Estado", max_length=45, blank=True, null=True)
    hide = models.BooleanField(default=0)

    def __str__(self):
        return self.status

    class Meta:
        managed = True
        verbose_name = 'Status de Fabricação'
        verbose_name_plural = 'Status de Fabricação'


class Statusvenda(models.Model):
    """ Status de venda """

    pkid_status = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.descricao

    class Meta:
        managed = True
        verbose_name = 'Status de Venda'
        verbose_name_plural = 'Status de Venda'


class Telefone(models.Model):
    """ Armazena informações de um telefone """

    pkid_telefone = models.AutoField(primary_key=True)
    fkid_pessoa = models.ForeignKey(
        'Pessoa', on_delete=models.CASCADE,
        verbose_name='Pessoa', null=True)
    ddi = models.CharField('DDI', max_length=3, blank=True, null=True, default=55)
    ddd = models.CharField('DDD', max_length=2, blank=True, null=True, default=11)
    numero = models.CharField('Número', max_length=15)
    hide = models.BooleanField(default=0)

    def __str__(self):
        return f'{self.numero}'

    class Meta:
        managed = True
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'


class Unidademedida(models.Model):
    """ Armazena Unidades de Medidas utilizadas no sistema """

    pkid_unidademedida = models.AutoField(primary_key=True)
    unidademedida = models.CharField('Unidade', max_length=50)
    hide = models.BooleanField(default=0)

    def __str__(self):
        return self.unidademedida

    class Meta:
        managed = True
        verbose_name = 'Unidade de Medida'
        verbose_name_plural = 'Unidades de Medida'


class Usuario(models.Model):
    """ Atualmente não está em uso """

    pkid_usuario = models.AutoField(primary_key=True)
    nomecompleto = models.CharField(max_length=45)
    login = models.CharField(unique=True, max_length=45)
    senha = models.CharField(max_length=45)
    dt_importacao = models.DateTimeField()
    dt_alteracao = models.DateTimeField()
    hide = models.BooleanField(default=0)

    class Meta:
        managed = True


class Usuarioalteracao(models.Model):
    """ Futuramente para realizar backups e logs """

    pkid_usuario_alteracao = models.AutoField(primary_key=True)
    dt_alteracao = models.DateTimeField()
    tipo_alteracao = models.TextField()

    class Meta:
        managed = True
