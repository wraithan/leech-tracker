from os.path import dirname, abspath, join

import dj_database_url

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
AUTHENTICATION_BACKENDS = (
    'django_browserid.auth.BrowserIDBackend',
)
DATABASES = {
    'default': dj_database_url.config(default='postgresql://localhost/leech')
}
DEBUG = True
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django_browserid',
    'leech.core',
)
LANGUAGE_CODE = 'en-us'
LOGIN_REDIRECT_URL_FAILURE = LOGIN_REDIRECT_URL = '/'
MANAGERS = ADMINS
MEDIA_ROOT = ''
MEDIA_URL = ''
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
ROOT_DIR = dirname(dirname(abspath(__file__ + '/../')))
ROOT_URLCONF = 'leech.urls'
SECRET_KEY = 'zb(n28@=gw3=1++%-x$71t*kws1j71611*$g&41a_+me%+6m^='
SITE_ID = 1
SITE_URL = 'http://localhost:8888'
STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATIC_ROOT = join(ROOT_DIR, 'static/')
STATIC_URL = '/static/'
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django_browserid.context_processors.browserid_form',
)
TEMPLATE_DEBUG = DEBUG
TEMPLATE_DIRS = ()
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = True
USE_L10N = True
USE_TZ = True
WSGI_APPLICATION = 'leech.wsgi.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {},
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'core': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django_browserid': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'requests': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}
