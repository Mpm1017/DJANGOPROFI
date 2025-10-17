from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verificamos si el usuario existe antes de autenticarlo
        if not User.objects.filter(username=username).exists():
            messages.error(request, "El usuario no existe. Por favor regístrate antes de ingresar.")
            return render(request, 'login.html')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Bienvenido, {user.username}")
            return redirect('panel')  # Redirige al panel principal
        else:
            messages.error(request, "Contraseña incorrecta. Inténtalo nuevamente.")
            return render(request, 'login.html')

    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'registro.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está registrado.')
            return render(request, 'registro.html')

        User.objects.create_user(username=username, password=password1)
        messages.success(request, 'Usuario creado correctamente. Ahora puedes iniciar sesión.')
        return redirect('login')

    return render(request, 'registro.html')
