from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import os

# =====================
# DOTENV VARIABLES

try: 
    load_dotenv(find_dotenv())
except Exception as e:
    print("No dotenv file found")

# =====================
# GENERAL PARAMETERS

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: Generated using secrets.token_hex(24)
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# SECURITY WARNING: Returns true when the environment variable is "True"
DEBUG = (os.environ.get("DJANGO_DEBUG_VALUE") == "True")

ALLOWED_HOSTS = [
    '127.0.0.1'
]


# =====================
# APP DEFINITION

INSTALLED_APPS = [
    'recipe_book.apps.RecipeBookConfig',
    'sass_processor',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'recipe_manager.urls'

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

WSGI_APPLICATION = 'recipe_manager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Set the static root for Heroku and Sass
# (Same root for both base and Sass)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
SASS_PROCESSOR_ROOT = STATIC_ROOT

# Static file finders for SASS
# See: https://engineertodeveloper.com/how-to-easily-use-sass-scss-with-django/
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# =====================
# Crispy Forms

# Tell crispy forms which template to use
CRISPY_TEMPLATE_PACK = 'bootstrap5'

# =====================
# Media

# Directory where the uploaded files will be saved
# (Profile_pics directory will be added inside media)
#   - BASE_DIR: Variable at the top of the settings file for projects directory
#   - 'media': Folder inside the base directory
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Public URL for the media route
MEDIA_URL = '/media/'

