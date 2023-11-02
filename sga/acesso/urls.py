from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('armazenar_senha/', views.armazenar_senha, name='armazenar_senha'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('exibir_senhas/', views.exibir_senhas, name='exibir_senhas'),
    path('adicionar_conta_senha/', views.adicionar_conta_senha, name='adicionar_conta_senha'),
    path('editar_conta_senha/', views.editar_conta_senha, name='editar_conta_senha'),


]