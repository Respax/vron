"""
Django settings for vron_new project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

##########################
# Imports
##########################
from django.utils.translation import ugettext_lazy as _
import os
#from celery.schedules import crontab





#########################################
# GENERAL SYSTEM CONFIGURATIONS
#########################################
# Base directory path
BASE_DIR = os.path.dirname( os.path.dirname( __file__ ) )

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&3je*i!yr=4y3sk&sm7^_/)fhd@^z7re&$y-b-wx(zsm3(6nyk'

# Path of wsgi app
WSGI_APPLICATION = 'vron.wsgi.application'

# User Model
AUTH_USER_MODEL = 'core.User'

# Login URL
LOGIN_URL = 'admin:login'






#########################################
# INTERNATIONALIZATION AND LOCALIZATION
#########################################
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Australia/Sydney'
USE_I18N = True
USE_L10N = True
USE_TZ = True





#########################################
# PATHS FOR STATIC, UPLOAD and TEMPLATES
#########################################
# Global UPLOAD folder
MEDIA_ROOT = os.path.join( BASE_DIR, '..', 'upload' )
MEDIA_URL = '/upload/'

# Statis Files paths
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join( BASE_DIR, '..', 'static' )

# Templates
TEMPLATE_DIRS = (
    os.path.join( BASE_DIR, '..', 'templates' ),
)

# The base URL Conf
ROOT_URLCONF = 'vron.urls'





#########################################
# TEMPLATE SETTINGS
#########################################

# Template Context Processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'vron.core.context_processors.add_global_template_data',
)





#########################################
# MIDDLEWARES
#########################################
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
)


#########################################
# DJANGO APPS REQUIRED
#########################################
# Application definition
DEFAULT_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
)
THIRD_PARTY_APPS = (
    # 'djcelery'
)
LOCAL_APPS = (
    'vron.core',
    'vron.admin',
    'vron.connector',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS





########################################
# Celery settings
#######################################
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
CELERYBEAT_SCHEDULE = {}





########################################
# Database Mapping Settings
########################################
ID_CONFIG_RON_USERNAME = 1
ID_CONFIG_RON_PASSWORD = 2
ID_CONFIG_RON_TEST_URL = 3
ID_CONFIG_RON_LIVE_URL = 4
ID_CONFIG_MAX_FAILED_ATTEMPTS = 5
ID_CONFIG_ERROR_EMAIL = 6
ID_CONFIG_BASE_API_KEY = 7

ID_LOG_STATUS_PENDING = 1
ID_LOG_STATUS_COMPLETE_APPROVED = 2
ID_LOG_STATUS_COMPLETE_REJECTED = 3
ID_LOG_STATUS_ERROR = 4