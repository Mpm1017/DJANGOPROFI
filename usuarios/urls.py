from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from . import views

app_name = 'usuarios'  # <-- Namespace registrado

urlpatterns = [
    # REDIRECCIÓN RAÍZ
    path('', RedirectView.as_view(url=reverse_lazy('usuarios:login'), permanent=False)),

    # AUTENTICACIÓN BÁSICA
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('panel/', views.panel, name='panel'),

    # RECUPERACIÓN DE CONTRASEÑA
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(
             template_name='usuarios/reset_password.html',
             success_url=reverse_lazy('usuarios:password_reset_done')
         ), 
         name='reset_password'),

    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='usuarios/password_reset_done.html'
         ), 
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='usuarios/reset_password_confirm.html',
             success_url=reverse_lazy('usuarios:password_reset_complete')
         ), 
         name='password_reset_confirm'),

    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='usuarios/password_reset_complete.html'
         ), 
         name='password_reset_complete'),
]
