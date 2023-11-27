from rest_framework import serializers
from acesso import models

class UsuariosSerializer(serializers.ModelSerializer):
    class meta:
        model = models.Usuarios
        fields ='__all__'

class SenhasContasSerializer(serializers.ModelSerializer):
    class meta:
        model = models.SenhasContas
        fields ='__all__'

class HistoricoSenhaSerializer(serializers.ModelSerializer):
    class meta:
        model = models.HistoricoSenha
        fields ='__all__'

