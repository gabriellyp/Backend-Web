from django.urls import path, include
from django.contrib import admin
from . import views
from usuarios import urls
urlpatterns = [
    path('', views.cadastro, name='cadastro'),
    path('login/', views.loginuser, name="login"),
    path('telaprincipal/', views.telaprincipal, name="telaprincipal"),
    
]

