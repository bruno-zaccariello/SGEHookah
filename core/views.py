from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from core.forms import Teste
import datetime

'''
#Modelo

@login_required(login_url="/Login")
@user_passes_test(checa_professor)
def page_cadastro_disciplina(request):
    if request.POST:
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            print("DISCIPLINA CADASTRADA")
    else:
        form = DisciplinaForm()
    context = {
        "form":form
    }
    return render(request,"CadastrarDisciplina.html",context)

'''

__all__ = ["index", "home", "redirect_home", "iframe_home", "cadastrar_produto", "user_main"]

# Create your views here.

def index(request):
	return render(request, "index.html")
	
def user_main(request):
	return render(request, "usuario/user_main.html")
	
@login_required(login_url="/admin")
def home(request):
	return render(request, "base.html")
	
def redirect_home(request):
	return redirect('/admin')
	
def iframe_home(request):
	return render(request, "iframe/home.html")
	
def cadastrar_produto(request):
	if request.POST:
		form = Teste(request.POST)
		if form.is_valid():
			form.save()
			print("DISCIPLINA CADASTRADA")
	else:
		form = Teste()
	context = {
			"form":form
	}
	return render(request, "iframe/produtos/cadastrar_produto.html", context)
