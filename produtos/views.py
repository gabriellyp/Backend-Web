from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Produtos
from django.urls import reverse

def index(request):
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
    n = request.POST["nomeprod"]
    m = request.POST["material"]
    t = request.POST["tamanho"]
    p = request.POST["preco"]
    q = request.POST["quantidade"]    

    produto = Produtos(nomeprod=n, material=m, tamanho=t, preco=p, quantidade=q)
    produto.save()
    return HttpResponseRedirect(reverse('index'))

def apagar(request, id):
  produto = Produtos.objects.get(id=id)
  produto.delete()
  return HttpResponseRedirect(reverse('index'))

def editar(request, id):
  produto = Produtos.objects.get(id=id)
  template = loader.get_template('editar.html')
  context = {
    'produto': produto,
  }
  return HttpResponse(template.render(context, request))

def editarproduto(request, id):
  n = request.POST["nomeprod"]
  m = request.POST["material"]
  t = request.POST["tamanho"]
  p = request.POST["preco"]
  q = request.POST["quantidade"]
  produto = Produtos.objects.get(id=id)
  produto.nomeprod = nomeprod
  produto.material = material
  produto.tamanho = tamanho
  produto.preco = preco
  produto.quantidade = quantidade
  produto.save()
  return HttpResponseRedirect(reverse('index'))
# Create your views here.
