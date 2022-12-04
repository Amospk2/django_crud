from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url='login/')
def home(request):
    users = User.objects.all()
    return render(request, 'index.html', {"users":users})

@login_required(login_url='login/')
def salvar(request):
    name = request.POST.get("name")
    user.objects.create(name=name)
    user = User.objects.all()
    return render(request, 'index.html', {"user":user})

@login_required(login_url='login/') 
def editar(request, id):
    user = User.objects.get(id=id)
    return render(request, 'update.html', {"user":user})

@login_required(login_url='login/')
def atualizar(request, id):
    email = request.POST.get("email")
    username = request.POST.get("username")
    first_name = request.POST.get("firstname")
    last_name = request.POST.get("lastname")
    senha = request.POST.get("senha")
    confirmar_senha = request.POST.get("confirmarsenha")
 
    user = User.objects.get(id=id)

    if user is not None and senha == confirmar_senha:
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.password = senha
        user.save()
        return redirect(home)
    else:
        messages.error(request=request, message="As senha não coicidem.")
        return redirect(editar, id=user.id)

@login_required(login_url='login/')
def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect(home)

