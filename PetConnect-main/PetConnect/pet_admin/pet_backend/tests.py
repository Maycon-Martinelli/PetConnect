from django.test import TestCase
from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('complemento_info', views.complemento_info, name='complemento_info'),
]

# Create your tests here.
