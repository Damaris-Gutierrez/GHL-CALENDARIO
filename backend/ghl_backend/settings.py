"""
Django settings for ghl_backend project.
"""

from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

# Inicializar entorno
env = environ.Env(
    DEBUG=(bool, False)
)

# Leer archivo .env (debe estar en la raíz del proyecto, junto a manage.py)
environ.Env.read_env(BASE_DIR / ".env")

# Clave y Debug desde .env
SECRET_KEY = env("DJANGO_SECRET_KEY", default="insecure-secret")
DEBUG = env("DEBUG", default=False)

# Private Token (para llamadas directas con la API de GHL)
GHL_PRIVATE_TOKEN = env("GHL_PRIVATE_TOKEN", default=None)
# 🔹 Base URL correcta para Private Token
GHL_BASE_URL = env("GHL_BASE_URL", default="https://rest.gohighlevel.com")
GHL_LOCATION_ID = env("GHL_LOCATION_ID", default=None)


ALLOWED_HOSTS = ["*"]  # Para desarrollo, en producción define tu dominio

# ---------------------------------------------------------
# Application definition
# ---------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",   # Para permitir peticiones desde React
    "ghl",           # Tu app personalizada
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # <- debe estar arriba de CommonMiddleware
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ghl_backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ghl_backend.wsgi.application"

# ---------------------------------------------------------
# Base de datos (SQLite en desarrollo)
# ---------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ---------------------------------------------------------
# Validaciones de contraseña
# ---------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ---------------------------------------------------------
# Idioma y zona horaria
# ---------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ---------------------------------------------------------
# Archivos estáticos
# ---------------------------------------------------------
STATIC_URL = "static/"

# Clave primaria por defecto
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ---------------------------------------------------------
# 🔹 Configuración de CORS para permitir peticiones desde React
# ---------------------------------------------------------
CORS_ALLOW_ALL_ORIGINS = True  # Permite acceso desde cualquier origen (solo en desarrollo)
# En producción usa:
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
#     "https://tu-dominio.com"
# ]
