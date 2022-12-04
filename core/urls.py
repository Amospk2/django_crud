from django.urls import path
from .views.home import home, salvar, editar, atualizar, delete
from .views.login import register, create_new_user, auth_user, logout_view, login_view

urlpatterns = [
    path('', home, name="home"),
    path('login/', login_view, name="login"),
    path('register/', register, name='register'),
    path('salvar/', salvar, name="salvar"),
    path('editar/<int:id>', editar, name="editar"),
    path('atualizar/<int:id>', atualizar, name="atualizar"),
    path('delete/<int:id>', delete, name="delete"),
    path('create_new_user/', create_new_user, name='create_new_user'),
    path('auth_user/', auth_user, name='auth_user'),
    path('logout/', logout_view, name='logout'),
]
