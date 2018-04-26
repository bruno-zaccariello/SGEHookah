# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bairro(models.Model):
    pkid_bairro = models.TextField(db_column='PKID_Bairro', unique=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bairro = models.CharField(db_column='Bairro', unique=True, max_length=45)  # Field name made lowercase.
    fkid_usuario = models.IntegerField(db_column='FKID_Usuario')  # Field name made lowercase.
    fkid_usuarioalteracao = models.IntegerField(db_column='FKID_UsuarioAlteracao')  # Field name made lowercase.
    dt_cadastro = models.TextField(db_column='DT_Cadastro')  # Field name made lowercase. This field type is a guess.
    dt_alteracao = models.TextField(db_column='DT_Alteracao')  # Field name made lowercase. This field type is a guess.
    hide = models.TextField(db_column='HIDE')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Bairro'


class Cargo(models.Model):
    pkid_cargo = models.TextField(db_column='PKID_Cargo', unique=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cargo = models.CharField(db_column='Cargo', max_length=45)  # Field name made lowercase.
    fkid_usuario = models.IntegerField(db_column='FKID_Usuario')  # Field name made lowercase.
    fkid_usuarioalteracao = models.IntegerField(db_column='FKID_UsuarioAlteracao')  # Field name made lowercase.
    dt_cadastro = models.TextField(db_column='DT_Cadastro')  # Field name made lowercase. This field type is a guess.
    dt_alteracao = models.TextField(db_column='DT_Alteracao')  # Field name made lowercase. This field type is a guess.
    hide = models.TextField(db_column='HIDE')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Cargo'


class Cidade(models.Model):
    pkid_cidade = models.TextField(db_column='PKID_Cidade', unique=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cidade = models.CharField(db_column='Cidade', unique=True, max_length=45)  # Field name made lowercase.
    fkid_estado = models.IntegerField(db_column='FKID_Estado')  # Field name made lowercase.
    fkid_usuario = models.IntegerField(db_column='FKID_Usuario')  # Field name made lowercase.
    fkid_usuarioalteracao = models.CharField(db_column='FKID_UsuarioAlteracao', max_length=45)  # Field name made lowercase.
    dt_cadastro = models.TextField(db_column='DT_Cadastro')  # Field name made lowercase. This field type is a guess.
    dt_alteracao = models.TextField(db_column='DT_Alteracao')  # Field name made lowercase. This field type is a guess.
    hide = models.TextField(db_column='HIDE')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Cidade'


class Email(models.Model):
    pkid_email = models.TextField(db_column='PKID_Email', unique=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    email = models.CharField(db_column='Email', unique=True, max_length=45)  # Field name made lowercase.
    fkid_pessoa = models.IntegerField(db_column='FKID_Pessoa')  # Field name made lowercase.
    fkid_usuario = models.IntegerField(db_column='FKID_Usuario')  # Field name made lowercase.
    fkid_alteracao = models.IntegerField(db_column='FKID_Alteracao')  # Field name made lowercase.
    dt_cadastro = models.TextField(db_column='DT_Cadastro')  # Field name made lowercase. This field type is a guess.
    dt_alteracao = models.TextField(db_column='DT_Alteracao')  # Field name made lowercase. This field type is a guess.
    hide = models.TextField(db_column='HIDE')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Email'


class Endereco(models.Model):
    pkid_endereco = models.TextField(db_column='PKID_Endereco', unique=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    logradouro = models.CharField(db_column='Logradouro', max_length=100)  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero')  # Field name made lowercase.
    complemento = models.CharField(db_column='Complemento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cep = models.IntegerField(db_column='CEP', blank=True, null=True)  # Field name made lowercase.
    tipoendereco = models.CharField(db_column='TipoEndereco', max_length=1)  # Field name made lowercase.
    fkid_cidade = models.IntegerField(db_column='FKID_Cidade')  # Field name made lowercase.
    fkid_bairro = models.IntegerField(db_column='FKID_Bairro')  # Field name made lowercase.
    fkid_pessoa = models.IntegerField(db_column='FKID_Pessoa')  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=250, blank=True, null=True)  # Field name made lowercase.
    hide = models.TextField(db_column='HIDE')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Endereco'


class Estado(models.Model):
    pkid_estado = models.TextField(db_column='PKID_Estado', unique=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    estado = models.CharField(db_column='Estado', unique=True, max_length=45)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', unique=True, max_length=2)  # Field name made lowercase.
    fkid_usuario = models.IntegerField(db_column='FKID_Usuario')  # Field name made lowercase.
    fkid_usuarioalteracao = models.IntegerField(db_column='FKID_UsuarioAlteracao')  # Field name made lowercase.
    dt_cadastro = models.TextField(db_column='DT_Cadastro')  # Field name made lowercase. This field type is a guess.
    dt_alteracao = models.TextField(db_column='DT_Alteracao')  # Field name made lowercase. This field type is a guess.
    hide = models.TextField(db_column='HIDE')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Estado'


class Estadocivil(models.Model):
    fkid_estadocivil = models.TextField(db_column='FKID_EstadoCivil', unique=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    estadocivil = models.CharField(db_column='EstadoCivil', unique=True, max_length=45)  # Field name made lowercase.
    fkid_usuario = models.IntegerField(db_column='FKID_Usuario')  # Field name made lowercase.
    fkid_usuarioalteracao = models.IntegerField(db_column='FKID_UsuarioAlteracao')  # Field name made lowercase.
    dt_cadastro = models.TextField(db_column='DT_Cadastro')  # Field name made lowercase. This field type is a guess.
    dt_alteracao = models.TextField(db_column='DT_Alteracao')  # Field name made lowercase. This field type is a guess.
    hide = models.TextField(db_column='HIDE')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EstadoCivil'


class Pessoa(models.Model):
    pkid_pessoa = models.TextField(db_column='PKID_Pessoa', unique=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nomecompleto_razaosocial = models.CharField(db_column='NomeCompleto_RazaoSocial', max_length=50)  # Field name made lowercase.
    apelido_nomefantasia = models.CharField(db_column='Apelido_NomeFantasia', max_length=50)  # Field name made lowercase.
    cpf_cnpj = models.CharField(db_column='CPF_CNPJ', unique=True, max_length=19)  # Field name made lowercase.
    rg_ie = models.CharField(db_column='RG_IE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gernero = models.CharField(db_column='Gernero', max_length=1)  # Field name made lowercase.
    dt_nascimento = models.DateField(db_column='DT_Nascimento', blank=True, null=True)  # Field name made lowercase.
    dt_cadastro = models.TextField(db_column='DT_Cadastro')  # Field name made lowercase. This field type is a guess.
    dt_alteracao = models.TextField(db_column='DT_Alteracao')  # Field name made lowercase. This field type is a guess.
    fkid_cargo = models.IntegerField(db_column='FKID_Cargo', blank=True, null=True)  # Field name made lowercase.
    fkid_estadocivil = models.IntegerField(db_column='FKID_EstadoCivil', blank=True, null=True)  # Field name made lowercase.
    fkid_ramoatividade = models.IntegerField(db_column='FKID_RamoAtividade', blank=True, null=True)  # Field name made lowercase.
    fkid_usuario = models.IntegerField(db_column='FKID_Usuario')  # Field name made lowercase.
    fkid_usuarioalteracao = models.IntegerField(db_column='FKID_UsuarioAlteracao')  # Field name made lowercase.
    st_pessoajuridica = models.TextField(db_column='ST_PessoaJuridica')  # Field name made lowercase. This field type is a guess.
    hide = models.TextField(db_column='HIDE')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Pessoa'


class PesssoaTipopessoa(models.Model):
    pkid_pessoatipopessoa = models.TextField(db_column='PKID_PessoaTipoPessoa', unique=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fkid_pessoa = models.IntegerField(db_column='FKID_Pessoa')  # Field name made lowercase.
    fkid_tipopessoa = models.IntegerField(db_column='FKID_TipoPessoa')  # Field name made lowercase.
    fkid_usuario = models.IntegerField(db_column='FKID_Usuario')  # Field name made lowercase.
    fkid_usuarioalteracao = models.IntegerField(db_column='FKID_UsuarioAlteracao')  # Field name made lowercase.
    dt_cadastro = models.TextField(db_column='DT_Cadastro')  # Field name made lowercase. This field type is a guess.
    dt_alteracao = models.TextField(db_column='DT_Alteracao')  # Field name made lowercase. This field type is a guess.
    hide = models.TextField(db_column='HIDE')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Pesssoa_TipoPessoa'


class Ramoatividade(models.Model):
    pkid_ramoatividade = models.TextField(db_column='PKID_RamoAtividade', unique=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ramoatividade = models.CharField(db_column='RamoAtividade', unique=True, max_length=45)  # Field name made lowercase.
    fkid_usuario = models.IntegerField(db_column='FKID_Usuario')  # Field name made lowercase.
    fkid_usuarioalteracao = models.IntegerField(db_column='FKID_UsuarioAlteracao')  # Field name made lowercase.
    dt_cadastro = models.TextField(db_column='DT_Cadastro')  # Field name made lowercase. This field type is a guess.
    dt_alteracao = models.TextField(db_column='DT_Alteracao')  # Field name made lowercase. This field type is a guess.
    hide = models.TextField(db_column='HIDE')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'RamoAtividade'


class Telefone(models.Model):
    pkid_telefone = models.TextField(db_column='PKID_Telefone', unique=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ddi = models.IntegerField(db_column='DDI')  # Field name made lowercase.
    ddd = models.IntegerField(db_column='DDD')  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero')  # Field name made lowercase.
    contato = models.CharField(db_column='Contato', max_length=45)  # Field name made lowercase.
    fkid_pessoa = models.IntegerField(db_column='FKID_Pessoa')  # Field name made lowercase.
    fkid_usuario = models.IntegerField(db_column='FKID_Usuario')  # Field name made lowercase.
    fkid_usuarioalteracao = models.IntegerField(db_column='FKID_UsuarioAlteracao')  # Field name made lowercase.
    dt_cadastro = models.TextField(db_column='DT_Cadastro')  # Field name made lowercase. This field type is a guess.
    dt_alteracao = models.TextField(db_column='DT_Alteracao')  # Field name made lowercase. This field type is a guess.
    hide = models.TextField(db_column='HIDE')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Telefone'
        unique_together = (('ddi', 'ddd', 'numero'),)


class Tipopessoa(models.Model):
    pkid_tipopessoa = models.TextField(db_column='PKID_TipoPessoa', unique=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tipopessoa = models.CharField(db_column='TipoPessoa', unique=True, max_length=45)  # Field name made lowercase.
    fkid_usuario = models.IntegerField(db_column='FKID_Usuario')  # Field name made lowercase.
    fkid_usuarioalteracao = models.CharField(db_column='FKID_UsuarioAlteracao', max_length=45)  # Field name made lowercase.
    dt_cadastro = models.TextField(db_column='DT_Cadastro')  # Field name made lowercase. This field type is a guess.
    dt_alteracao = models.TextField(db_column='DT_Alteracao')  # Field name made lowercase. This field type is a guess.
    hide = models.TextField(db_column='HIDE')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'TipoPessoa'


class Usuario(models.Model):
    pkid_usuario = models.TextField(db_column='PKID_Usuario', unique=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fkid_usuario = models.IntegerField(db_column='FKID_Usuario')  # Field name made lowercase.
    nomecompleto = models.CharField(db_column='NomeCompleto', max_length=45)  # Field name made lowercase.
    login = models.CharField(db_column='Login', unique=True, max_length=45)  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=45)  # Field name made lowercase.
    dt_cadastro = models.TextField(db_column='DT_Cadastro')  # Field name made lowercase. This field type is a guess.
    dt_alteracao = models.TextField(db_column='DT_Alteracao')  # Field name made lowercase. This field type is a guess.
    hide = models.TextField(db_column='HIDE')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Usuario'


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
    id = models.IntegerField(primary_key=True)
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
    last_modified = models.DateTimeField(blank=True, null=True)

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
