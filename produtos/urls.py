from django.urls import path
from . import views
urlpatterns = [
    path('homeadm/', views.homeadm, name='homeadm'),
    path('homeadm/adicionar/', views.adicionar, name='adicionar'),
    path('homeadm/adicionar/addproduto/', views.addproduto, name='addproduto'),
    path('homeadm/apagar/<int:id>', views.apagar, name='apagar'),
    path('homeadm/editar/<int:id>', views.editar, name='editar'),
    path('homeadm/editar/editarproduto/<int:id>', views.editarproduto, name='editarproduto'),
]
