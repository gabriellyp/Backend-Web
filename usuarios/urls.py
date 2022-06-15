from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.cadastro, name='cadastro'),
    path('login/', views.login, name="login"),
    path('telaprincipal/', views.telaprincipal, name="telaprincipal"),
]

