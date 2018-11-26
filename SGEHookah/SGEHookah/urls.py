"""SGEHookah URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path
import core.views as view
import core.my_views.vendas as vendas
from django.contrib.auth import views as auth_views

urls_usuario = [
    path('', view.user_main, name="user_main"),
    path('AlterarSenha', view.change_pw_form, name="user_alterar_senha"),
    path('AlterarInfo', view.update_user_form, name="update_user_form")
]

urls_clientes = [
    path('cadastrar/', view.cadastrar_cliente, name="cadastrar_cliente"),
    path('cadastrar/cadastro_rapido/', view.cadastro_rapido_cliente,
         name="cadastro_rapido_cliente"),
    path('<int:id_cliente>/', view.editar_cliente, name="editar_cliente"),
    path('lista/', view.lista_clientes, name="lista_clientes"),
    path('deletar/<int:id_cliente>/', view.deletar_cliente, name="deletar_cliente")
]

urls_produtos = [
    path('cadastrar/', view.CadastrarProduto.as_view(), name="cadastrar_produto"),
    path('<int:id_produto>/', view.PaginaProduto.as_view(), name="product_page"),
    path('<int:id_produto>/formula/', view.formula_produto, name="formula_produto"),
    path('lista/', view.lista_produtos, name="lista_produtos"),
    path('deletar/<int:id_produto>/', view.deletar_produto, name="deletar_produto"),
    path('materia/cadastrar/', view.cadastrar_materia, name="cadastrar_materia"),
    path('materia/lista/', view.lista_materia, name="lista_materia"),
    path('materia/<int:id_materia>/', view.editar_materia, name="editar_materia"),
    path('materia/deletar/<int:id_materia>', view.deletar_materia, name="deletar_materia"),
    path('categorias/', view.lista_categorias, name="lista_categorias"),
    path('categorias/deletar/<int:id_categoria>/',
         view.deletar_categoria, name="deletar_categoria"),
    path('categorias/<int:id_categoria>/', view.editar_categoria, name="editar_categoria"),
    path('unidades/', view.lista_unidades, name="lista_unidades"),
    path('unidades/deletar/<int:id_unidade>/',
         view.deletar_unidade, name="deletar_unidade"),
    path('unidades/<int:id_unidade>/', view.editar_unidade, name="editar_unidade")
]

urls_producao = [
    path('formulas/lista/', view.lista_formula, name="lista_formulas"),
    path('formulas/deletar/<int:id_formula>',
         view.deletar_formula, name="deletar_formula"),
    path('formulas/<int:id_formula>/', view.pagina_formula, name="pagina_formula"),
    path('pedidos/', view.lista_fabricacao, name="lista_fabricacao"),
    path('pedidos/novo/', view.nova_fabricacao, name="nova_fabricacao"),
    path('pedidos/<int:id_fabricacao>/',
         view.editar_fabricacao, name="editar_fabricacao"),
    path('pedidos/deletar/<int:id_fabricacao>', view.deletar_fabricacao, name="deletar_fabricacao")
]

urls_vendas = [
    path('', vendas.ListaVendas.as_view(), name="lista_vendas"),
    path('nova/', vendas.NovaVenda.as_view(), name="nova_venda"),
    path('deletar/<int:id_venda>', vendas.DeletarVenda.as_view(), name="deletar_venda"),
]

urls_fornecedores = [
    path('cadastrar/', view.cadastrar_fornecedor, name="cadastrar_fornecedor"),
    path('lista/', view.lista_fornecedores, name="lista_fornecedores"),
    path('deletar/<int:id_fornecedor>/', view.deletar_fornecedor, name="deletar_fornecedor"),
    path('<int:id_fornecedor>/', view.editar_fornecedor, name="editar_fornecedor"),
]

api = [
    path('valida_fabricacao/<int:id_formula>', view.valida_fabricacao, name="valida_fabricacao"),
    path('get_produto/', view.get_produto, name="get_produto"),
    path('search_produto/', view.search_produto, name="search_produto"),
]

urlpatterns = [
    path('admindjango/', admin.site.urls),
    path('admin/', auth_views.LoginView.as_view(template_name='index.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page="/")),
    path('admin/home/', view.home, name="home"),
    path('', view.redirect_home),
    path('iframe/home/', view.iframe_home, name="iframe_home"),
    path('iframe/produtos/', include(urls_produtos)),
    path('admin/usuario/', include(urls_usuario)),
	path('iframe/fornecedores/', include(urls_fornecedores)),
    path('iframe/clientes/', include(urls_clientes)),
    path('iframe/producao/', include(urls_producao)),
    path('iframe/vendas/', include(urls_vendas)),
    path('iframe/vendas/calcula_frete/', view.calcula_frete, name="calcula_frete"),

    path('api/', include(api)),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
