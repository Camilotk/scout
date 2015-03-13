# -*- coding:utf-8 -*-
"""
Django settings for hypercamp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = BASE_DIR
#PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Admin user: guerra pass: g
ADMINS = (
    ('Rober Guerra', 'roberzguerra@gmail.com'),
)

MANAGERS = ADMINS

# Application definition
INSTALLED_APPS = (
    'bootstrap_admin',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.webdesign',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'bootstrap3',
    'ckeditor',
    'filebrowser',
    'registration',
    'core',
    'institution',
    'scout_group',
    'campotec',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'core.exceptions.middleware.ExceptionMiddleware',
)

ROOT_URLCONF = 'scout.urls'

WSGI_APPLICATION = 'scout.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'scout.db', # Or path to database file if using sqlite3: os.path.join(BASE_DIR, 'db.sqlite3'),
        #'USER': 'postgres', # Not used with sqlite3.
        #'PASSWORD': '', # Not used with sqlite3.
        #'HOST': 'localhost', # Set to empty string for localhost. Not used with sqlite3.
        #'PORT': '5432', # Set to empty string for default. Not used with sqlite3.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #os.path.join(BASE_DIR, "static"),
    ('', os.path.join(BASE_DIR, 'bootstrap_admin', 'static')),
    ('', os.path.join(BASE_DIR, 'ckeditor', 'static')),
    ('', os.path.join(BASE_DIR, 'filebrowser', 'static')),
    ('', os.path.join(BASE_DIR, 'institution', 'static')),
    ('', os.path.join(BASE_DIR, 'sitestatic')),
)

SERVER_STATIC_FILES = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'filebrowser', 'templates'),
    os.path.join(BASE_DIR, 'registration', 'templates'),
    os.path.join(BASE_DIR, 'bootstrap_admin', 'templates'),
    os.path.join(BASE_DIR, 'institution', 'templates'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
MEDIA_URL = '/media/'

# User model
#AUTH_USER_MODEL = 'core.models.CoreUser'

# App bootstrap_admin
# For Sidebar Menu (List of apps and models) (RECOMMENDED)
from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    # "institution.context_processors.menu_loader",
    # "institution.context_processors.navigation",
)
BOOTSTRAP_ADMIN_SIDEBAR_MENU = True

# CKEditor Configuration
CKEDITOR_UPLOAD_PATH = os.path.join("uploads")
CKEDITOR_UPLOAD_DIRECTORY_DATE = True
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 300,
    },
    'description': {
        'autoParagraph': False,
        'width': 'auto',
        'height': 200,
        'toolbarCanCollapse': True,
        'filebrowserWindowWidth': 800,
        'filebrowserWindowHeight': 600,
        'filebrowserImageBrowseUrl': '/admin/filebrowser/browse?pop=3',
        'filebrowserBrowseUrl': '/admin/filebrowser/browse?pop=3',
        'toolbar':[
            ["StrikeThrough","-","Undo","Redo","-","Cut","Copy","Paste","PasteText","PasteFromWord","Find","Replace","-",
                "Outdent","Indent","NumberedList","BulletedList"],
            ["-", "JustifyLeft", "JustifyCenter", "JustifyRight", "JustifyBlock"], ["Source", "Maximize"],
            ["Format","Font","FontSize","TextColor","BGColor","-","Bold","Italic","Underline","RemoveFormat", "-","Image","Table","-","Link","Flash","-","Scayt"],
        ]
    },
    'title': {
        'autoParagraph': False,
        # 'toolbar': 'full',
        'width': 'auto',
        'height': 80,
        'toolbarCanCollapse': True,
        'filebrowserWindowWidth': 'auto',
        'filebrowserWindowHeight': 'auto',
        'toolbar':[
            ["Source"],
            ["StrikeThrough","-","Undo","Redo","-","Cut","Copy","Paste"],
            ["-","JustifyLeft","JustifyCenter","JustifyRight","JustifyBlock"],
            ["Format","Font","FontSize","TextColor","BGColor","-","Bold","Italic","Underline","-","Image","-","Link","-","Scayt"],
        ]
    },
}


# Registration Configuracoes
ACCOUNT_ACTIVATION_DAYS = 7 # limite de dias para a ativacao da conta
REGISTRATION_AUTO_LOGIN = True # SE True, os usuarios sao automaticamente logados ao clicar no link de ativacao da conta enviado por email. Default eh False
REGISTRATION_OPEN = False


# Configuracoes de email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' #Envia email real
EMAIL_HOST = 'smtp.gmail.com' #default='localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' #Envia um email no console (terminal)
#EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend' #nao envia email (não faz nada)

# GRUPOS DE USUARIO
# 1 - Admin - permissão total
# 2 - Lobinho - inscrição em especialidades do ramo lobinho
# 3 - Escoteiro - inscrição em especialidades do ramo escoteiras
# 4 - Sênior - Inscrição em especialidades do ramo sênior

try:
    from settings_server import *
except:
    pass