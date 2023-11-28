"""
URL configuration for sga project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from acesso.api import viewsets as usuariosViewsets
from acesso.api import viewsets as senhasContasViewSet
from acesso.api import viewsets as HistoricoSenhaViewSet

route = routers.DefaultRouter()

route.register(r'usuarios', usuariosViewsets.UsuariosViewSet, basename='Usuarios')
route.register(r'historicoSenhas',HistoricoSenhaViewSet.HistoricoSenhaViewSet, basename='HistoricoSenha')
route.register(r'senhasContas', senhasContasViewSet.SenhasContasViewSet, basename='SenhasContas')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('acesso.urls')),
    path('api/',include(route.urls))
]
