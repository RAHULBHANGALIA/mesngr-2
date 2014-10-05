"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    'C:\Users\rahi\Desktop\djng\mysite\prjctapp\templates',
    #PROJECT_PATH + '/templates/',
    #BASE_DIR + '/templates/'
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wj48j+fw_wmr**u0zy_$&dh$00h_i7j#8e%zqtr%em^k-+@59h'

# SECURITY WARNING: don't run with debug turned on in production!
from os.path import dirname,join
DEBUG = True

TEMPLATE_DEBUG = True
    
TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader','django.template.loaders.app_directories.Loader')

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'prjctapp',
    'rest_framework'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST':'localhost',
        'PORT':'3306',
        'NAME': 'projectapp2',
        'USER':'root',
        'PASSWORD':'rahul@4123',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS =( os.path.join(BASE_DIR, 'static'),'C:/Users/rahi/Desktop/djng/mysite/prjctapp/templates/static')

MEDIA_ROOT=join(BASE_DIR,'media')
MEDIA_URL='/media/'
MAX_UPLOAD_SIZE=20971520
CONTENT_TYPES=['application/pdf','image/jpeg','image/png','audio/mp3']

