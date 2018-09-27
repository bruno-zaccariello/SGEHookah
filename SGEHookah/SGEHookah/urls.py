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
from core.views import *
from django.contrib.auth.views import login, logout

usuario = [
    path('', user_main, name="user_main"),
    path('AlterarSenha', change_pw_form, name="user_alterar_senha"),
    path('AlterarInfo', update_user_form, name="update_user_form")
]

clientes = [
    path('cadastrar/', cadastrar_cliente, name="cadastrar_cliente"),
    path('cadastrar/cadastro_rapido/', cadastro_rapido_cliente,
         name="cadastro_rapido_cliente"),
    path('<int:id_cliente>/', editar_cliente, name="editar_cliente"),
    path('lista/', lista_clientes, name="lista_clientes"),
    path('deletar/<int:id_cliente>/', deletar_cliente, name="deletar_cliente")
]

produtos = [
    path('cadastrar/', cadastrar_produto, name="cadastrar_produto"),
    path('<int:id_produto>/', product_page, name="product_page"),
    path('<int:id_produto>/formula/', formula_produto, name="formula_produto"),
    path('lista/', lista_produtos, name="lista_produtos"),
    path('deletar/<int:id_produto>/', deletar_produto, name="deletar_produto"),
    path('materia/cadastrar/', cadastrar_materia, name="cadastrar_materia"),
    path('materia/lista/', lista_materia, name="lista_materia"),
    path('materia/<int:id_materia>/', editar_materia, name="editar_materia"),
    path('categorias/', lista_categorias, name="lista_categorias"),
    path('categorias/deletar/<int:id_categoria>/',
         deletar_categoria, name="deletar_categoria"),
    path('unidades/', lista_unidades, name="lista_unidades"),
    path('unidades/deletar/<int:id_unidade>/',
         deletar_unidade, name="deletar_unidade")
]

producao = [
    path('formulas/lista/', lista_formula, name="lista_formulas"),
    path('formulas/deletar/<int:id_formula>',
         deletar_formula, name="deletar_formula"),
    path('formulas/<int:id_formula>/', pagina_formula, name="pagina_formula"),
    path('pedidos/', lista_fabricacao, name="lista_fabricacao"),
    path('pedidos/novo/', nova_fabricacao, name="nova_fabricacao"),
    path('pedidos/<int:id_fabricacao>/',
         editar_fabricacao, name="editar_fabricacao"),
]

api = [
    path('nova_fabricacao/', ajax_nova_fabricacao, name="ajax_nova_fabricacao"),
    path('checa_materias/', ajax_checa_materias, name="ajax_checa_materias"),
]

urlpatterns = [
    path('admindjango/', admin.site.urls),
    path('admin/', login, {"template_name": "index.html"}, name="login"),
    path('logout/', logout, {'next_page': 'login'}, name="logout"),
    path('admin/home/', home, name="home"),
    path('', redirect_home),
    path('iframe/home/', iframe_home, name="iframe_home"),
    path('iframe/produtos/', include(produtos)),
    path('admin/usuario/', include(usuario)),
    path('iframe/clientes/', include(clientes)),
    path('iframe/producao/', include(producao)),
    path('iframe/vendas/calcula_frete/', calcula_frete, name="calcula_frete"),

    path('api/', include(api)),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
