from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('registro/', views.register_view, name='register'),
    path('panel/', views.panel_view, name='panel'),
    path('logout/', views.logout_view, name='logout'),
    path('reset-password/', views.reset_password_view, name='reset_password'),  # 👈 nueva ruta
]

