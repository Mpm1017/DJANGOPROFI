from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # puedes cambiar 'home' por la vista que tengas
]
