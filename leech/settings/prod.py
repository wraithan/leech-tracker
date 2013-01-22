from os import getenv

from .base import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG
STATIC_URL = 'http://media.leechtracker.net/static/'
SITE_URL = 'leechtracker.net'
SENTRY_DSN = getenv('SENTRY_DSN', None)

INSTALLED_APPS += ('gunicorn',)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
           'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
