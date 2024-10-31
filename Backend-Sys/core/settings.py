
from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv()
DBUSER = os.getenv("DBUSER")
DBNAME = os.getenv("DBNAME")
DBPASS = os.getenv("DBPASS")
DBHOST = os.getenv("DBHOST")
DBPORT = os.getenv("DBPORT")
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = []


INSTALLED_APPS = [
 "django.contrib.admin",
 "django.contrib.auth",
 "django.contrib.contenttypes",
 "django.contrib.sessions",
 "django.contrib.messages",
 "django.contrib.staticfiles",
    "analytics",
    "policy_management",
    "authentication",
    "compliance_management",
    "reporting",
    "audit_log",
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
  'DIRS':[],  'APP_DIRS':True, 
  'OPTIONS':{"context_processors": [
                          "django.template.context_processors.debug",
                          "django.template.context_processors.request",
                          "django.contrib.auth.context_processors.auth",
                          "django.contrib.messages.context_processors.messages"]}}]
WSGI_APPLICATION = "core.wsgi.application"
DATABASES = {"default": {
              'ENGINE': "django.db.backends.postgresql",
              'NAME': DBNAME,
              'USER': DBUSER,
              'PASSWORD': DBPASS,
              'HOST': DBHOST,
              'PORT': DBPORT}}

AUTH_PASSWORD_VALIDATORS = [
 {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
 {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
 {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
 {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"}]
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ASGI_APPLICATION = 'core.asgi.application' 

# Celery configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'  
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'  

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}