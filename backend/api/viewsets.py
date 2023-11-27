from rest_framework import viewsets
from api import serializers
from acesso import models

class UsuariosViewSet(viewsets.ModelViewSet):
    serializers_class = serializers.UsuariosSerializer
    queryset = models.Usuarios.objects.all()


class SenhasContasViewSet(viewsets.ModelViewSet):
    serializers_class = serializers.SenhasContasSerializer
    queryset = models.SenhasContas.objects.all()


class HistoricoSenhaViewSet(viewsets.ModelViewSet):
    serializers_class = serializers.HistoricoSenhaSerializer
    queryset = models.HistoricoSenha.objects.all()