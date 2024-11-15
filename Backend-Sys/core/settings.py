from pathlib import Path
from urllib.parse import urlparse
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Parse the DATABASE_URL from environment variables
# DATABASE_URL = os.getenv("DATABASE_URL")
# if not DATABASE_URL:
#     raise ValueError("DATABASE_URL environment variable not set.")

# Use urlparse to extract components from the DATABASE_URL
#tmpPostgres = urlparse(DATABASE_URL)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'datashield_solutions',
        'USER': 'neondb_owner',
        'PASSWORD': 'UPl4zXyeag8u',
        'HOST': 'ep-floral-smoke-a5i5ll2m.us-east-2.aws.neon.tech',
        'PORT': '5432',  # Default PostgreSQL port
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable not set.")

# Debugging settings
DEBUG = os.getenv("DEBUG", "False") == "True"  # Use environment variable for debug
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")  # Use environment variable for allowed hosts

# CORS settings
CORS_ALLOW_ALL_ORIGINS = DEBUG  # Allow all origins in development
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000", 
]

# Application definition
INSTALLED_APPS = [
    "analytics",
    "policy_management",
    "authentication",
    "compliance_management",
    "reporting",
    "audit_log",
    "ingestion",

    'rest_framework',
    'rest_framework.authtoken',  
    'django_otp',
    'django_otp.plugins.otp_totp',

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'corsheaders',
]

FRONTEND_URL = 'http://localhost:3000'  

# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'redeemed751@gmail.com' 
# EMAIL_HOST_PASSWORD = 'print("hello world");' 
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware', 
    'django_otp.middleware.OTPMiddleware',
]

ROOT_URLCONF = "core.urls"

# Template settings
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

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Localization settings
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files settings
STATIC_URL = "static/"
# Uncomment and configure if needed
# STATIC_ROOT = os.path.join(BASE_DIR.parent, 'staticfiles')
# STATICFILES_DIRS = [os.path.join(BASE_DIR.parent, 'frontend/ds-react/build/static')]

# Default auto field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ASGI_APPLICATION = 'core.asgi.application' 

# Celery configuration
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')  
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [(os.getenv('REDIS_HOST', '127.0.0.1'), int(os.getenv('REDIS_PORT', 6379)))],
        },
    },
}

# REST framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day', 
        'user': '1000/day', 
    },
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,  
}