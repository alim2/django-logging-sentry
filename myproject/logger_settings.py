LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s  %(asctime)s  %(module)s '
                      '%(process)d  %(thread)d  %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',  # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': 'logs/logging.log'
        }
    },
    'loggers': {
        'error': {
            'level': 'ERROR',
            'handlers': ['file'],
            'propagate': False,
        }
    },
}
