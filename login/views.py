from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

# Vista para iniciar sesión
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Verifica si el usuario existe
        if not User.objects.filter(username=username).exists():
            return render(request, 'login.html', {'error': 'Usuario no existe, por favor regístrate primero'})
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('panel')
        else:
            return render(request, 'login.html', {'error': 'Contraseña incorrecta'})
    return render(request, 'login.html')

# Vista para registrar usuarios
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'El usuario ya existe'})
        
        if password != password2:
            return render(request, 'register.html', {'error': 'Las contraseñas no coinciden'})
        
        User.objects.create_user(username=username, password=password)
        messages.success(request, 'Usuario creado con éxito')
        return redirect('login')

    return render(request, 'register.html')

# Vista para el panel principal
@login_required
def panel_view(request):
    return render(request, 'panel.html')

# Vista para cerrar sesión
def logout_view(request):
    logout(request)
    return redirect('login')


# 🆕 NUEVA vista para restablecer contraseña
def reset_password_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not User.objects.filter(username=username).exists():
            return render(request, 'reset_password.html', {'error': 'El usuario no existe'})

        if new_password != confirm_password:
            return render(request, 'reset_password.html', {'error': 'Las contraseñas no coinciden'})

        user = User.objects.get(username=username)
        user.set_password(new_password)
        user.save()

        return render(request, 'login.html', {'success': 'Contraseña cambiada con éxito. Inicia sesión nuevamente.'})

    return render(request, 'reset_password.html')
