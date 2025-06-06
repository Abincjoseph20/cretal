import os
from pathlib import Path
from decouple import config
import dj_database_url
from django.contrib.messages import constants as messages

# Build paths

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-dxprkqfd1jw%mq-=)#my9ot*2f#qsv3a&3_hp8yjf00^bki@ih'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['cretal.onrender.com', '127.0.0.1', 'localhost']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainapp',
    'carts',
    'accounts',
    'orders',
    
    'cloudinary',
    'cloudinary_storage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'whitenoise.middleware.WhiteNoiseMiddleware',
    
]

ROOT_URLCONF = 'cretal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'template')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'carts.context_processor.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'cretal.wsgi.application'

# Database configuration

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'cretal',
#         'USER': 'postgres',
#         'PASSWORD': '',  # Replace with your actual password
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# DATABASE_URL = config('DATABASE_URL', default='')
# if DATABASE_URL:
#     DATABASES = {
#         'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
#     }
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
#             'NAME': config('DB_NAME', default='cretal'),
#             'USER': config('DB_USER', default='postgres'),
#             'PASSWORD': config('DB_PASSWORD', default=''),
#             'HOST': config('DB_HOST', default='localhost'),
#             'PORT': config('DB_PORT', default='5432'),
#         }
#     }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    # ... (keep your existing validators)
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Authentication
AUTH_USER_MODEL = 'accounts.Account'
LOGIN_REDIRECT_URL = '/profile/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
from django.contrib.messages import constants as messages


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587  # Or the appropriate port for your SMTP serverAdd commentMore actions
EMAIL_USE_TLS = config('EMAIL_USE_TLS',cast=bool) # Use TLS for secure communication
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': config('CLOUDINARY_API_KEY'),
    'API_SECRET': config('CLOUDINARY_API_SECRET')
}

# EMAIL_USE_TLS=True
# EMAIL_HOST_USER='EMAIL_HOST_USER'
# EMAIL_HOST_PASSWORD='EMAIL_HOST_PASSWORD'

