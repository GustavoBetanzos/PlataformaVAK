from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Usuario


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)
            return redirect('dashboard')

        else:

            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'login.html')


def register_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')

        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        if password != confirm_password:

            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('register')

        if Usuario.objects.filter(username=username).exists():

            messages.error(request, 'El usuario ya existe')
            return redirect('register')

        user = Usuario.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)

        return redirect('dashboard')

    return render(request, 'crearCuenta.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def logout_view(request):

    logout(request)
    return redirect('login')