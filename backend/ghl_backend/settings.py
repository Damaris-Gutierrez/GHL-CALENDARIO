import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # carga .env

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "cambia-esto"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",   # 👈 para CORS
    "ghl",           # 👈 tu app
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # 👈 importante, arriba de CommonMiddleware
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
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
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ghl_backend.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LANGUAGE_CODE = "es-es"
TIME_ZONE = "America/Lima"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 👇 Variables personalizadas

# URL base de GHL
GHL_BASE_URL = "https://services.leadconnectorhq.com"

# Token privado (Private Integration Token de tu subcuenta)
GHL_PRIVATE_TOKEN = "pit-5b57cd65-6de3-4681-9a11-a9de464a8db6"

# LocationId de tu subcuenta (requerido por la API)
GHL_LOCATION_ID = "r3UrTfNuQviYjKT9vfVz"



CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # React Vite
    "http://localhost:3000",  # React CRA
]
