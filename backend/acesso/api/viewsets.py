from rest_framework import viewsets
from .serializers import *
from acesso.models import *

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer


class SenhasContasViewSet(viewsets.ModelViewSet):
    serializer_class = SenhasContasSerializer
    queryset = SenhasContas.objects.all()


class HistoricoSenhaViewSet(viewsets.ModelViewSet):
    serializer_class = HistoricoSenhaSerializer
    queryset = HistoricoSenha.objects.all()