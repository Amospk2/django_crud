from django.contrib import messages
from django.contrib.auth import authenticate, logout, login, get_user
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from ..views import home

def is_guess(use):
    if not use.is_authenticated:
        return True
    else:
        return False

def login_view(request):
    return render(request, 'login.html') if is_guess(request.user) else redirect(home.home)


def register(request):
    return render(request, 'register.html') if is_guess(request.user) else redirect(home.home)

def auth_user(request):
    username =request.POST.get('username')
    senha = request.POST.get('senha')
    if(username is not None and senha is not None):
        user = authenticate(username=username, password=senha)
    else:
        messages.error(request=request, message="Preenche essa merda")
        return render(request, 'login.html')

    if user is not None:
        login(request, user)
        return redirect(home.home)
    else:
        messages.error(request=request, message="Informações incorretas")
        return render(request, 'login.html')

def create_new_user(request):
    email = request.POST.get('email')
    username = request.POST.get('username')
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    senha = request.POST.get('senha')
    confirmarsenha = request.POST.get('confirmarsenha')

    if(email != None and username != None  and firstname != None and firstname != None and senha != None):
        messages.error(request=request, message="Preencha todos os campos")

    if(senha != confirmarsenha):
        messages.error(request=request, message="As senha não coicidem.")
        return redirect(register)
    
    user = User.objects.create_user(username=username, email=email, password=senha)
    user.first_name = firstname
    user.last_name = lastname
    user.save()
    
    return redirect(login_view)

def logout_view(request):
    logout(request)
    return redirect(login_view)


