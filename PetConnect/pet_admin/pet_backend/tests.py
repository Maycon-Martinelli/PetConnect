from django.test import TestCase
from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
]

# Create your tests here.