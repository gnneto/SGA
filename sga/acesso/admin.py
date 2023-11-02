from django.contrib import admin
from .models import Usuarios, SenhasContas, HistoricoSenha

# Register your models here.

admin.site.register(Usuarios)
admin.site.register(SenhasContas)
admin.site.register(HistoricoSenha)


