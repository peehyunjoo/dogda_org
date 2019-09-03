"""
Django settings for dogda project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import django_heroku       #debug.log를 할려면 헤로쿠 자체를 빼야 debug.log가 생김!
from dogda.info_settings import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'j4b=r!q-kz5vyz%s)z8p59r76&x@xwjwo&u@3+7i$4v1&$s=_2'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '(j4b=r!q-kz5vyz%s)z8p59r76&x@xwjwo&u@3+7i$4v1&$s=_2')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#ALLOWED_HOSTS = ['localhost','127.0.0.1','herokuapp.com']
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oauth.apps.OauthConfig',
    'info.apps.InfoConfig',
    'bootstrap4'
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

ROOT_URLCONF = 'dogda.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'dogda.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER':'',
        'PASSWORD': '',
        'HOST': 'pizzudb.cfjiog4ayfky.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306',
        'OPTIONS': {
        'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': NAME,
        'USER':USER,
        'PASSWORD': PASSWORD,
        'HOST': HOST,
        'PORT': PORT,
        'OPTIONS': {
        'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_FORMAT='Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i:s'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

LOGGING = {
    'version':1,
    'disable_existing_loggers':False,   #기존의 로그설정을 비활서화 할것인지
    'handlers':{
        # 로그 파일을 만들어 텍스트로 로그레코드 저장
        'file':{
            'level':'DEBUG',
            'class':'logging.FileHandler',
            'filename':'debug.log',
            #'filename':'../myLog.log'
        },
        #콘솔에 출력
        'console':{
            'level': 'DEBUG',
            'class' : 'logging.StreamHandler'
        }
    },
    'loggers':{
        'django':{
            'handlers':['file'],
            'level':'DEBUG',
            'propagate':True,
        },
    },
}

django_heroku.settings(locals())
