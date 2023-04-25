from pathlib import Path
import os
import django
from django.utils.encoding import smart_str
django.utils.encoding.smart_text = smart_str

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = '0a-ad1=wneqwxowj=ji%a%5@v1+xl=$*sgdl$zvim7-+0h^k(l'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
  

    # allauth
    'django.contrib.sites',
    
  

    # Applications
    'xhtml2pdf',
    'taggit',
    'user_visit',
    'debug_toolbar',
    'ckeditor',
    'enterprise',
    "cvbuilder",
    'corsheaders',
    "jobapp"
]

CKEDITOR_CONFIGS = {
    'CVBuilder_Config': {
        'toolbar': [
            {'name' : 'basic', 'items' : ['Bold', 'Italic', 'Underline', 'Strike']},
            {'name': 'colors', 'items': ['TextColor']},
            {'name': 'paragraph', 'items': ['JustifyLeft', 'JustifyBlock']},
        ],
        'height' : 245,
        'width': '100%',
        'enterMode': 2,
    },
    'default': {
        'width': '100%',
        'tabSpaces': 4,

    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'project-config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, 'templates')),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # All Auth
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'project-config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},]

# allauth
SITE_ID = 1
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
AUTH_USER_MODEL="cvbuilder.User"

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
CORS_ORIGIN_ALLOW_ALL = True
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
