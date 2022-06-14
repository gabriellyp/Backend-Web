from django.db import models
class Produtos(models.Model):
  nomeprod = models.CharField(max_length=255)
  material = models.CharField(max_length=255)
  tamanho = models.CharField(max_length=100)
  preco = models.CharField(max_length=8)
  quantidade = models.CharField(max_length=5)
  

# Create your models here.

