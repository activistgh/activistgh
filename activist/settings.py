"""
Django settings for activist project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from dotenv import load_dotenv

load_dotenv()
import json
from pathlib import Path
from google.oauth2 import service_account 
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@2$0_1o%$cz3!&^1+lyogky93_z#(*$j)-k5d*iir2$3_7eugi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", ".vercel.app", ".now.sh",'cpsdeliverygh.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'shop',
    'crispy_forms',
    'payment',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'activist.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'activist.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "verceldb",
        'URL_NO_SSL':"postgres://default:l6pfZtQ0nFbW@ep-noisy-smoke-a4lu5tos-pooler.us-east-1.aws.neon.tech:5432/verceldb",
        "URL":"postgres://default:l6pfZtQ0nFbW@ep-noisy-smoke-a4lu5tos-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require",
        "PRISMA_URL":"postgres://default:l6pfZtQ0nFbW@ep-noisy-smoke-a4lu5tos-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require&pgbouncer=true&connect_timeout=15",
        "URL_NON_POOLING":"postgres://default:l6pfZtQ0nFbW@ep-noisy-smoke-a4lu5tos.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require",
        'USER': "default",
        'PASSWORD':"l6pfZtQ0nFbW",
        "HOST":"ep-noisy-smoke-a4lu5tos-pooler.us-east-1.aws.neon.tech"
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
#comment out the old db

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True






# #Google Cloud Storage settings
# GS_PROJECT_ID = 'precise-line-437900-m9'
# GS_BUCKET_NAME = 'activistimages'

# # Get the JSON key data from environment variable
# google_cloud_key = os.getenv('KEY')

# # Parse the JSON key
# google_cloud_info = json.loads(google_cloud_key)

# # settings.py
# DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
# GS_CREDENTIALS = service_account.Credentials.from_service_account_info(
#     google_cloud_info
# )

# # Media files (uploads)
# GS_MEDIA_BUCKET_NAME = GS_BUCKET_NAME
# MEDIA_URL = f'https://storage.googleapis.com/{GS_MEDIA_BUCKET_NAME}/'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'productionFiles'

MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Get public and secret key from env

PAYSTACK_SECRET_KEY = os.getenv('PAYSTACK_SECRET_KEY')

PAYSTACK_PUBLIC_KEY = os.getenv('PAYSTACK_PUBLIC_KEY')