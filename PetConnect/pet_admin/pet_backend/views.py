from django.shortcuts import render
from django.http import HttpResponse

def home(request): 
    return render(request, 'html/home.html', {'logo': 'image/petconnect.svg'})

def login(request):
    return render(request, 'html/login.html', {'logo': 'image/petconnect.svg'})

def cadastro(request):
    return render(request, 'html/cadastro.html', {'logo': 'image/petconnct.svg'})
# Create your views here.
