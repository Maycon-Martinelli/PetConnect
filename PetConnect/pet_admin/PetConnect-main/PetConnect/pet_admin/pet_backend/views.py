from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import teste, teste_complemento

valor0 = 0
valor1 = 0

def home(request): 
    return render(request, 'html/home.html', {'logo': 'image/petconnect.svg'})

def login(request):
    global valor0
    if request.method == 'POST':
        print("teste")
        for email in teste.objects.all():
            if request.POST.get('email') == email.email and request.POST.get('password') == email.senha:
                valor0 = email.id
                return redirect (complemento_info)
            else:
                return redirect(login)
    return render(request, 'html/login.html', {'logo': 'image/petconnect.svg'})

def cadastro(request): 
            #delete do banco
    for delete in teste.objects.all():
        if delete.id == 11:
            print(delete.id)
            teste.objects.get(pk=delete.id).delete()

    if request.method == 'POST':
        teste_save= teste(
            nome=request.POST.get('name'),
            email=request.POST.get('email'),
            senha=request.POST.get('password'),
            telefone=request.POST.get('phone'),
            cidade=request.POST.get('city'),
        )
        teste_save.save()
        return redirect(login)
    return render(request, 'html/cadastro.html', {'logo': 'image/petconnct.svg'})



def complemento_info(request):
    global valor0
    print(valor0)
    for verificacao in teste_complemento.objects.all():
            if verificacao.id_id == valor0:
                return redirect(home)
            
    if request.method == 'POST':
        
            
        teste_save= teste_complemento(
            id_id=valor0,
            cpf=request.POST.get('cpf'),
            date=request.POST.get('date'),
            cep=request.POST.get('cep'),
            estado=request.POST.get('estado'),
            endereco=request.POST.get('endereco'),
            rua=request.POST.get('rua'),
            numero=request.POST.get('numero'),
            complemento=request.POST.get('complemento')
        )
        teste_save.save()
        return redirect(home)
    
    return render(request, 'html/complemento_info.html', {'logo': 'image/petconnct.svg'})


# Create your views here.
