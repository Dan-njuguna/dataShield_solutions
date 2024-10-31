# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Susan\OneDrive\Desktop\datashield solutions\Backend-Sys\core\settings.py
# Compiled at: 2024-10-30 15:45:55
# Size of source mod 2**32: 3293 bytes
# I wanted to use this https://pypi.org/project/python-decouple/
# What does it do? I am not so vast with it..lemme check docs ASAP
# let me show you the syntax it's easier to use and cleaner
# It's that simple
# are you there?
# migrate the other apps 1 by 1 when testing then you will get the one causing errors.


from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config("SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = []


INSTALLED_APPS = [
 "django.contrib.admin",
 "django.contrib.auth",
 "django.contrib.contenttypes",
 "django.contrib.sessions",
 "django.contrib.messages",
 "django.contrib.staticfiles",
 "authentication",
 "analytics",
 "policy_management",
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

DATABASES = {
    "default": {
              'ENGINE': "django.db.backends.postgresql",
              'NAME': config("DBNAME"),
              'USER': config("DBUSER"),
              'PASSWORD': config("DBPASS"),
              'HOST': config("DBHOST"),
              'PORT': config("DBPORT")
            }
            }

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
# CELERY_BROKER_URL = 'redis://localhost:6379/0'  
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'  

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [('127.0.0.1', 6379)],
#         },
#     },
# }