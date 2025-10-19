import os
from pathlib import Path
from django.urls import reverse_lazy
from dotenv import load_dotenv

# ================================
# BASE DEL PROYECTO
# ================================
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()

# ================================
# CONFIGURACIONES GENERALES
# ================================
SECRET_KEY = 'django-insecure-($+e4yq9%b@i(x1b0uwbr$xf(_$!e=#hk&p%0w!eag)fpp*9y_'
DEBUG = True
ALLOWED_HOSTS = []

# ================================
# APLICACIONES INSTALADAS
# ================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contadores',
    'usuarios',
]

# ================================
# MIDDLEWARE
# ================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ================================
# URLS Y TEMPLATES
# ================================
ROOT_URLCONF = 'miweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'miweb.wsgi.application'

# ================================
# BASE DE DATOS
# ================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

# ================================
# VALIDACIÓN DE CONTRASEÑAS
# ================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ================================
# AUTENTICACIÓN
# ================================
LOGIN_URL = reverse_lazy('usuarios:login')
LOGIN_REDIRECT_URL = reverse_lazy('usuarios:panel')
LOGOUT_REDIRECT_URL = reverse_lazy('usuarios:login')

# ================================
# CONFIGURACIÓN DE CORREO ELECTRÓNICO
# ================================
# Para pruebas locales sin enviar emails reales:
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Para producción con SMTP real:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# ================================
# ARCHIVOS ESTÁTICOS
# ================================
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# ================================
# ARCHIVOS MEDIA
# ================================
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
