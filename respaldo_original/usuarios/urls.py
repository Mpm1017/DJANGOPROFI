from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('panel/', views.panel, name='panel'),
    path('reset_password/', views.reset_password_view, name='reset_password'),
    path('reset_password_confirm/<str:token>/', views.reset_password_confirm_view, name='reset_password_confirm'),
]



