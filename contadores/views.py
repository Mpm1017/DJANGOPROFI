from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# 🔹 Vista para iniciar sesión
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('panel')
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'login.html')

# 🔹 Vista para el panel principal
@login_required
def panel_view(request):
    return render(request, 'panel.html')

# 🔹 Vista para cerrar sesión
def logout_view(request):
    logout(request)
    return redirect('login')


