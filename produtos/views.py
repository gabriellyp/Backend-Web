from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Produtos
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User

def homeadm(request):
  listaProdutos = Produtos.objects.all().values()
  template = loader.get_template('homeadm.html')
  context = {
    'listaProdutos': listaProdutos,
  }
  return HttpResponse(template.render(context, request))

def adicionar(request):
  template = loader.get_template('adicionar.html')
  return HttpResponse(template.render({}, request))

def addproduto(request):
    nomeprod = request.POST["nomeprod"]
    material = request.POST["material"]
    tamanho = request.POST["tamanho"]
    preco = request.POST["preco"]
    quantidade = request.POST["quantidade"]    

    produto = Produtos(nomeprod=nomeprod,material=material,tamanho=tamanho,preco=preco,quantidade=quantidade)
    produto.save()
    return HttpResponseRedirect(reverse('homeadm'))

def apagar(request, id):
  produto = Produtos.objects.get(id=id)
  produto.delete()
  return HttpResponseRedirect(reverse('homeadm'))

def editar(request, id):
  produto = Produtos.objects.get(id=id)
  template = loader.get_template('editarprod.html')
  context = {
    'produto': produto,
  }
  return HttpResponse(template.render(context, request))

def editarproduto(request, id):
  nomeprod = request.POST["nomeprod"]
  material = request.POST["material"]
  tamanho = request.POST["tamanho"]
  preco = request.POST["preco"]
  quantidade = request.POST["quantidade"]
  produto = Produtos.objects.get(id=id)
  produto.nomeprod = nomeprod
  produto.material = material
  produto.tamanho = tamanho
  produto.preco = preco
  produto.quantidade = quantidade
  produto.save()
  return HttpResponseRedirect(reverse('homeadm'))
# Create your views here.
