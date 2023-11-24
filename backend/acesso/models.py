from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Usuarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    logAtividade = models.DateTimeField(auto_now_add=True)
    AutMFA = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user}'



class SenhasContas(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    senhaContasHash = models.CharField(max_length=128)
    nomeContaVic = models.CharField(max_length=50)

    def __str__(self):
        return f'Usuario: {self.usuario} | {self.nomeContaVic}'


class HistoricoSenha(models.Model):
    senha_conta = models.ForeignKey(SenhasContas, on_delete=models.CASCADE)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataAlteracao = models.DateTimeField(auto_now=True)
    senhaAntiga = models.CharField(max_length=128)

