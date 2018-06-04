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
	path('AlterarSenha', altera_senha_form, name="user_alterar_senha"),
	path('AlterarInfo', atualiza_user_form, name="atualiza_user_form")
]

produtos = [
	path('cadastrar/', cadastrar_produto, name="cadastrar_produto"),
	path('<int:id_produto>', pagina_produto, name="pagina_produto"),
	path('lista/', lista_produtos, name="lista_produtos"),
	path('deletar/<int:id_produto>', deletar_produto, name="deletar_produto"),
	path('categorias/', lista_categorias, name="lista_categorias"),
	path('categorias/deletar/<int:id_categoria>', deletar_categoria, name="deletar_categoria"),
	path('unidades/', lista_unidades, name="lista_unidades"),
	path('unidades/deletar/<int:id_unidade>', deletar_unidade, name="deletar_unidade")
]

urlpatterns = [
  path('admindjango/', admin.site.urls),
	path('admin/', login, {"template_name":"index.html"}, name="login"),
	path('logout/', logout, {'next_page':'login'}, name="logout"),
	path('admin/home/', home, name="home"),
	path('', redirect_home),
	path('iframe/home/', iframe_home, name="iframe_home"),
	path('iframe/produtos/', include(produtos)),
	path('admin/usuario/', include(usuario)),
	path('iframe/vendas/calcula_frete', calcula_frete, name="calcula_frete")
]

if settings.DEBUG is True:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)