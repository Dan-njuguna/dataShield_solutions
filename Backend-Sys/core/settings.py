from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

DBUSER = os.getenv("DBUSER", "default_user")
DBNAME = os.getenv("DBNAME", "db")
DBPASS = os.getenv("DBPASS", "default_pass")
DBHOST = os.getenv("DBHOST", "localhost")
DBPORT = os.getenv("DBPORT", "5432")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True
ALLOWED_HOSTS = []

# Application definition
CORS = {
    "ALLOW_ALL_ORIGINS": True,
    "ALLOW_ALL_HEADERS": True,
    "ALLOW_ALL_METHODS": True,
}

# Allowing all origins, headers and methods
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  
]


INSTALLED_APPS = [
    "analytics",
    "policy_management",
    "authentication",
    "compliance_management",
    "reporting",
    "audit_log",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'corsheaders',
 ]


MIDDLEWARE = [
 "django.middleware.security.SecurityMiddleware",
 "django.contrib.sessions.middleware.SessionMiddleware",
 "django.middleware.common.CommonMiddleware",
 "django.middleware.csrf.CsrfViewMiddleware",
 "django.contrib.auth.middleware.AuthenticationMiddleware",
 "django.contrib.messages.middleware.MessageMiddleware",
 "django.middleware.clickjacking.XFrameOptionsMiddleware"]

ROOT_URLCONF = "core.urls"
TEMPLATES = [
    {'BACKEND':"django.template.backends.django.DjangoTemplates", 
    'DIRS': [os.path.join(BASE_DIR, "frontend/src")],
    'APP_DIRS':True,
    'OPTIONS':{
        "context_processors": [
            "django.template.context_processors.debug",
            "django.template.context_processors.request",
            "django.contrib.auth.context_processors.auth",
            "django.contrib.messages.context_processors.messages"
            ]
        }
    }
]
WSGI_APPLICATION = "core.wsgi.application"
DATABASES = {
    "default": {
              'ENGINE': "django.db.backends.postgresql",
              'NAME': DBNAME,
              'USER': DBUSER,
              'PASSWORD': DBPASS,
              'HOST': DBHOST,
              'PORT': DBPORT
              }
}

AUTH_PASSWORD_VALIDATORS = [
        {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
        {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
        {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
        {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"}
    ]


LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
# STATIC_ROOT = (os.path.join(BASE_DIR.parent, 'staticfiles'))
# STATICFILES_DIRS = [os.path.join(BASE_DIR.parent, 'Frontend-Sys/ds-react/build/static')]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ASGI_APPLICATION = 'core.asgi.application' 

# Celery configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'  
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}