from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from relatorios.models import Relatorio

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Esse nome de usuário já existe')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Esse e-mail já está sendo usado')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, 
                    first_name=first_name, last_name=last_name)
                    # Login apos cadastrar
                    # auth.login(request, user)
                    # messages.success(request, 'Você agora está logado no sistema')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'Você agora está cadastrado e pode fazer login')
                    return redirect('login')
        else:
            messages.error(request, 'As senhas não conferem')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Você agora está logado no sistema')
            return redirect('dashboard')
        else:
            messages.error(request, 'Dados Inválidos')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Você agora está deslogado')
    return redirect('index')

def dashboard(request):
    current_user = request.user
    rel = Relatorio.objects.all().order_by('-data_relatorio').filter(is_published=True, user_id=current_user.id)

    context = {
        'relatorios': rel
    }

    return render(request, 'accounts/dashboard.html', context)