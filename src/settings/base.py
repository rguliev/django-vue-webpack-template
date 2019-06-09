"""
Django base settings common for both dev and production environments
"""

import os
from dotenv import load_dotenv

def reduce_path(file_name, times):
    """Return the path of `times` parent directory."""
    result = os.path.realpath(file_name)
    for _ in range(times):
        result = os.path.dirname(result)
    return result

# Root dir of the project
ROOT_DIR = reduce_path(__file__, times=4)
# Backend dir
BASE_DIR = reduce_path(__file__, times=3)
TEMPLATES_DIR = os.path.join(ROOT_DIR, 'templates')
FRONTEND_DIR = os.path.join(ROOT_DIR, 'frontend')

# load settings from .env file
dotenv_path = os.path.join(ROOT_DIR, '.env')
load_dotenv(dotenv_path)

DEBUG = bool(int(os.getenv('DEBUG', False)))

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(',')

# Application definitions
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #THIRD_PARTY_APPS
    'rest_framework',
    'webpack_loader',
    #LOCAL_APPS
    'firstapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR, ],
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

WSGI_APPLICATION = 'src.wsgi.application'


# Database
# DATABASES = {...}

# Password validation
# AUTH_PASSWORD_VALIDATORS = [...]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
STATICFILES_DIRS = [
    os.path.join(ROOT_DIR, 'public'),
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Webpack settings
WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'STATS_FILE': os.path.join(FRONTEND_DIR, 'webpack-stats.json'),
    }
}