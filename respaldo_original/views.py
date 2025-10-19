from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "El usuario no existe. Por favor regístrate.")
            return render(request, 'usuarios/login.html')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Bienvenido, {user.username}")
            return redirect('panel')
        else:
            messages.error(request, "Contraseña incorrecta.")
            return render(request, 'usuarios/login.html')

    return render(request, 'usuarios/login.html')


# Registro
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, 'usuarios/register.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe.")
            return render(request, 'usuarios/register.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo ya está registrado.")
            return render(request, 'usuarios/register.html')

        User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, "Usuario creado correctamente. Ahora inicia sesión.")
        return redirect('login')

    return render(request, 'usuarios/register.html')


# Logout
def logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect('login')


# Panel protegido
@login_required
def panel(request):
    return render(request, 'usuarios/panel.html')
# Olvidé mi contraseña
def reset_password_view(request):
    return render(request, 'usuarios/reset_password.html')


from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string

# ===========================
# RECUPERAR CONTRASEÑA
# ===========================
def reset_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # 1️⃣ Verificar que el correo exista
        if not User.objects.filter(email=email).exists():
            messages.error(request, "No hay una cuenta asociada a ese correo.")
            return render(request, 'usuarios/reset_password.html')

        # 2️⃣ Crear un token simple
        token = get_random_string(32)
        user = User.objects.get(email=email)
        user.last_name = token  # lo guardamos temporalmente en el campo last_name
        user.save()

        # 3️⃣ Generar el enlace de restablecimiento
        reset_link = f"http://127.0.0.1:8000/reset_password_confirm/{token}/"

        # 4️⃣ Enviar el correo
        send_mail(
            subject="Recupera tu contraseña",
            message=f"Hola, haz clic en este enlace para restablecer tu contraseña:\n{reset_link}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )

        messages.success(request, "Te hemos enviado un enlace de recuperación a tu correo.")
        return redirect('login')

    return render(request, 'usuarios/reset_password.html')
def reset_password_confirm_view(request, token):
    try:
        user = User.objects.get(last_name=token)
    except User.DoesNotExist:
        messages.error(request, "El enlace no es válido o ya ha sido usado.")
        return redirect('login')

    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, 'usuarios/reset_password_confirm.html')

        user.set_password(password1)
        user.last_name = ""  # limpiar token
        user.save()

        messages.success(request, "Tu contraseña ha sido restablecida correctamente.")
        return redirect('login')

    return render(request, 'usuarios/reset_password_confirm.html')
