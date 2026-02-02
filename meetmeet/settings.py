import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# --- PATH CONFIGURATION ---
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Load environment variables from .env file
load_dotenv()

# --- SECURITY SETTINGS ---
SECRET_KEY = os.getenv('SECRET_KEY')

# DEBUG should be False in production
DEBUG = False

# Render.com specific host configuration
ALLOWED_HOSTS = ['.onrender.com'] if not DEBUG else ['*']


# --- APPLICATION DEFINITION ---
# Grouped by: Django built-ins, Third-party apps, and Local apps
INSTALLED_APPS = [
    # Django built-ins
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Third-party apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_bootstrap5',

    # Local apps
    'meetups',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Must be high in the list
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'meetmeet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',  # Allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'meetmeet.wsgi.application'


# --- DATABASE CONFIGURATION ---
# Uses dj_database_url to parse the DATABASE_URL environment variable
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600
    )
}


# --- AUTHENTICATION & ALLAUTH ---
# allauth uses the Sites framework
SITE_ID = 1

# Auth Redirection
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Email settings for allauth
ACCOUNT_EMAIL_VERIFICATION = 'none'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]


# --- INTERNATIONALIZATION ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# --- STATIC FILES CONFIGURATION ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Production specific static storage (WhiteNoise)
if not DEBUG:
    # Compresses and hashes files for caching efficiency
    STATICFILES_STORAGE = (
        'whitenoise.storage.CompressedManifestStaticFilesStorage'
    )

# --- MISCELLANEOUS ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
