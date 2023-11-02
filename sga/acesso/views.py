from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import SenhasContas, Usuarios
from django.shortcuts import get_object_or_404
from .forms import EditarContaForm

def index(request):
    
    return render(request, 'index.html')

def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe')
            return redirect('registro')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email já está em uso')
            return redirect('registro')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            Usuarios.objects.create(user=user)
            user.save()
            messages.success(request, 'Usuário registrado com sucesso')
            return redirect('login')
    else:
        return render(request, 'registro.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = get_user_model().objects.filter(email=email).first()
        if user is not None:
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Senha invalida')
        else:
            messages.error(request, 'Email não encontrado')
        return redirect('login')
    else:
        return render(request, 'login.html')


def armazenar_senha(request):
    if request.method == 'POST':
        nomeContaVic = request.POST['nomeContaVic']
        senhaContasHash = request.POST['senhaContasHash']
        usuario = Usuarios.objects.get(user=request.user)

        SenhasContas.objects.create(usuario=usuario, nomeContaVic=nomeContaVic, senhaContasHash=senhaContasHash)

        messages.success(request, 'Senha armazenada com sucesso')
        return redirect('index')
    else:
        return render(request, 'armazenar_senha.html')
    


def exibir_senhas(request):
    usuario = Usuarios.objects.get(user=request.user)
    senhas_contas = SenhasContas.objects.filter(usuario=usuario)

    return render(request, 'exibir_senhas.html', {'senhas_contas': senhas_contas})



def adicionar_conta_senha(request):
    if request.method == 'POST':
        nomeContaVic = request.POST['nomeContaVic']
        senhaContasHash = request.POST['senhaContasHash']
        usuario = Usuarios.objects.get(user=request.user)

        SenhasContas.objects.create(usuario=usuario, nomeContaVic=nomeContaVic, senhaContasHash=senhaContasHash)

        messages.success(request, 'Conta e senha adicionadas com sucesso')
        return redirect('adicionar_conta_senha')
    else:
        return render(request, 'adicionar_conta_senha.html')
    


def editar_conta_senha(request):
    if request.method == 'POST':
        form = EditarContaForm(request.user, request.POST)
        if form.is_valid():
            conta_senha = form.cleaned_data.get('conta')
            nova_senha = form.cleaned_data.get('nova_senha')
            conta_senha.senhaContasHash = nova_senha
            conta_senha.save()
            messages.success(request, 'Senha editada com sucesso')
    else:
        form = EditarContaForm(request.user)

    return render(request, 'editar_conta_senha.html', {'form': form})

