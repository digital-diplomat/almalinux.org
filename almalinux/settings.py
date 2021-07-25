"""
Django settings for almalinux project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

# TODO: .env support for all major settings that could change between envs

from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
from typing import List, Tuple, Union, Any

from dotenv import dotenv_values

BASE_DIR = Path(__file__).resolve().parent.parent
DOTENV = dotenv_values(BASE_DIR / '.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = DOTENV['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DOTENV['DEBUG'] == 'true'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'almalinux.org',
    'www.almalinux.org',
    'staging.almalinux.org',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_quill',
    'commons',
    'almalinux.apps.AlmaLinuxAdminConfig',
    'www',
]

MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'almalinux.urls'

template_loaders: List[Any] = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
]

effective_loaders: List[Union[str, Tuple]]

if DEBUG:
    effective_loaders = template_loaders
else:
    effective_loaders = [
        ('django.template.loaders.cached.Loader', template_loaders),
    ]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': [],
        'OPTIONS': {
            'loaders': effective_loaders,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'commons.context.dnt.is_dnt_enabled'
            ],
        },
    },
]

WSGI_APPLICATION = 'almalinux.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': DOTENV['DB_ENGINE'],
        'NAME': DOTENV['DB_NAME'],
        'USER': DOTENV['DB_USER'],
        'PASSWORD': DOTENV['DB_PASSWORD'],
        'HOST': DOTENV['DB_HOST'],
        'PORT': int(DOTENV['DB_PORT']),  # type: ignore
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    # ('de', 'Deutsch'),
    ('en', 'English'),  # English (US), default
    # ('es', 'Español'),  # Spanish (ES)
    ('fr', 'Français'),
    # ('he', 'עִבְרִית'), # Hebrew
    ('it', 'Italiano'),
    # ('ja', '日本語'),  # Japanese
    ('lv', 'Latviešu'),
    ('pl', 'Polski'),
    # ('pt', 'Português'),  # Portuguese (PT)
    ('pt-br', 'Português Brasileiro'),  # Portuguese (BR)
    ('ru', 'Русский'),
    ('tr', 'Türkçe'),
    ('uk', 'Украї́нська'),

)

LOCALE_PATHS = [
    BASE_DIR / 'locale'
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'public/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

ENCORE_BUILD_DIR = BASE_DIR / 'static/build/'

MEDIA_ROOT = BASE_DIR / 'media' if 0 == len(DOTENV['MEDIA_ROOT']) else DOTENV['MEDIA_ROOT']  # type: ignore
MEDIA_URL = 'media/'

# Custom settings
HUBSPOT_APIKEY = DOTENV['HUBSPOT_APIKEY']
HUBSPOT_SUB_ID = DOTENV['HUBSPOT_SUB_ID']

# Quill editor
QUILL_CONFIGS = {
    'default': {
        'theme': 'snow',
        'modules': {
            'syntax': True,
            'toolbar': [
                [
                    {'font': []},
                    {'header': []},
                    {'align': []},
                    'bold',
                    'italic',
                    'underline',
                    'strike',
                    'blockquote',
                    {'color': []},
                    {'background': []},
                    {'list': 'ordered'},
                    {'list': 'bullet'},
                ],
                ['code-block', 'link', 'image'],
                ['clean'],
            ],
        },
    }
}
