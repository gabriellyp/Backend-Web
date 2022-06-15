from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from usuarios import urls
from produtos import models


def cadastro(request):
  if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('telaprincipal')
  else:
        form_usuario = UserCreationForm()
  context = {'form_usuario': form_usuario}
  return render(request, 'cadastrar.html', context)

def loginuser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('telaprincipal')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})

def telaprincipal(request):
    listaProdutos = models.Produtos.objects.all().values()
    context = {
       'listaProdutos': listaProdutos,
    }
    return render(request, 'telaprincipal.html')


def sair(request):
    logout(request)
    return HttpResponseRedirect('loginuser.html')
# Create your views here.
