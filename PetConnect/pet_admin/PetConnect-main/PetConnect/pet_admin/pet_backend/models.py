# models.py
from django.db import models

class teste(models.Model):
    nome=models.CharField(max_length=50, blank=None)
    email=models.CharField(max_length=250, blank=None)
    senha=models.CharField(max_length=50, blank=None)
    tipo=models.CharField(max_length=50, default=0)
    telefone=models.IntegerField()
    cidade=models.CharField(max_length=50, blank=None)

class teste_complemento(models.Model):
    id_id=models.IntegerField(default=0)
    cpf=models.CharField(max_length=11, blank=None)
    date=models.CharField(max_length=10, null=False)
    cep=models.CharField(max_length=10, blank=None)
    estado=models.CharField(max_length=50, blank=None)
    endereco=models.CharField(max_length=50, blank=None)
    rua=models.CharField(max_length=50, blank=None)
    numero=models.IntegerField(blank=None)
    complemento=models.CharField(max_length=50, default='desconhecido')

class teste_ong(models.Model):
    id_id=models.IntegerField(default=0)
    cnpj=models.CharField(max_length=11, blank=None)
    date=models.CharField(max_length=10, null=False)
    cep=models.CharField(max_length=10, blank=None)
    estado=models.CharField(max_length=50, blank=None)
    endereco=models.CharField(max_length=50, blank=None)
    rua=models.CharField(max_length=50, blank=None)
    numero=models.IntegerField(blank=None)
    complemento=models.CharField(max_length=50, default='desconhecido')

# Create your models here.
