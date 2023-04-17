"""
Django settings for server project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path

CACHE_TTL = 60 * 15
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

AUTH_USER_MODEL = 'user.BaseUser'
AUTHENTICATION_BACKENDS = (
	'user.backends.EmailOrJustIDModelBackend',
	'rest_framework.authentication.TokenAuthentication',
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-z_(@+3l0nzt84a0o@tbt9k$owqvuo5toswg=hklolutt0-u_dh'
SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = int(os.environ.get("DEBUG", default=0))

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
CSRF_TRUSTED_ORIGINS = ['http://localhost:1337']
# Application definition

INSTALLED_APPS = [
	"daphne",
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'rest_framework',
	'rest_framework.authtoken',
	'corsheaders',
	'user',
	'request',
	'channels_permissions',
	'location',
	'chat',
	'report',
	'myadmin'
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',

	'corsheaders.middleware.CorsMiddleware',

]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
	{
		'BACKEND' : 'django.template.backends.django.DjangoTemplates',
		'DIRS'    : [],
		'APP_DIRS': True,
		'OPTIONS' : {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

ASGI_APPLICATION = "server.asgi.application"
WSGI_APPLICATION = 'server.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
	# 'default': {
	#     'ENGINE': 'django.db.backends.sqlite3',
	#     'NAME': BASE_DIR / 'db.sqlite3',
	# }
	'default': {
		"ENGINE"  : "django.db.backends.postgresql",
		"NAME"    : "postgres",
		"USER"    : "postgres",
		"PASSWORD": "postgres",
		"HOST"    : "db",  # set in docker-compose.yml
		"PORT"    : os.getenv("ENV_POSTGRES_PORT", 5432),  # default postgres port
	}

}
REDIS_HOST_PRIMARY = "redis://redis-master:" + os.getenv("ENV_REDIS_PORT", "6379")

CACHES = {
	"default": {
		"BACKEND"   : "django_redis.cache.RedisCache",
		"LOCATION"  : [REDIS_HOST_PRIMARY,
		               "redis://redis-slave:6380"
		               ],

		"OPTIONS"   : {
			"CLIENT_CLASS": "django_redis.client.DefaultClient"
		},
		"KEY_PREFIX": "server"
	}
}

CACHE_PREFIXES = {
	"REQUEST"  : {
		"STATUS": "request_status_*"
	},
	"LOCATION" : {
		"VOLUNTEER"   : "location_volunteer_*",
		"SPECIALNEEDS": "location_specialneeds_*",
	},
	"VOLUNTEER": {
		"STATUS": "volunteer_status_*"
	}
}



CHANNEL_LAYERS = {
	"default": {
		"BACKEND": "channels_redis.core.RedisChannelLayer",
		"CONFIG" : {
			"hosts": [REDIS_HOST_PRIMARY],
		},
	},
}
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': [
		'rest_framework.authentication.BasicAuthentication',
		'rest_framework.authentication.SessionAuthentication',
		'rest_framework.authentication.TokenAuthentication',

	],
	'DEFAULT_PAGINATION_CLASS'      : 'rest_framework.pagination.PageNumberPagination',
	'PAGE_SIZE'                     : 10
}

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://redis-broker:6381")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BACKEND", "redis://redis-master:6379")
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS = 0