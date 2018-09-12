LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s -> %(asctime)s %(module)s : %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': 'logs/logging.log'
        }
    },
    'loggers': {
        'logger_name': {
            'handlers': ['file'],
            'propagate': True,
        }
    },
}
