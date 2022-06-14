from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('adicionar/addproduto/', views.addproduto, name='addproduto'),
    path('apagar/<int:id>', views.apagar, name='apagar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('editar/editarproduto/<int:id>', views.editarproduto, name='editarproduto'),
]
