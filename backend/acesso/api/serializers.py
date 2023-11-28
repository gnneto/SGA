from rest_framework import serializers
from acesso.models import *

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields ='__all__'

class SenhasContasSerializer(serializers.ModelSerializer):
    class Meta:
        model = SenhasContas
        fields ='__all__'

class HistoricoSenhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoSenha
        fields ='__all__'

