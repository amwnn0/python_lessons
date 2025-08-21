import logging
import sys


from aiogram_lessons.logging_3_filter import ErrorLogFilter, CriticalLogFilter, DebugWarningFilter

logging_config = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {'format': '#%(levelname)-8s %(name)s:%(funcName)s - %(message)s'
        },
        'formatter1': {'format': '[%(asctime)s] #%(levelname)-8s %(filename)s:'
                      '%(lineno)d - %(name)s:%(funcName)s - %(message)s'
        },
        'formatter2': {'format': '#%(levelname)-8s [%(asctime)s] - %(filename)s:'
                      '%(lineno)d - %(name)s:%(funcName)s - %(message)s'
        }
    },
    'filters': {
        'critical_filter': {
            '()': CriticalLogFilter,
        },
        'error_filter': {
            '()': ErrorLogFilter,
        },
        'debug_warning_filter': {
            '()': DebugWarningFilter,
        }
    },
    'handlers': {
        'default': {
            'class': logging.StreamHandler,
            'formatter': 'default'
        },
        'stderr': {
            'class': logging.StreamHandler,
        },
        'stdout': {
            'class': logging.StreamHandler,
            'formatter': 'formatter2',
            'filters': ['debug_warning_filter'],
            'stream': sys.stdout
        },
        'error_file': {
            'class': logging.FileHandler,
            'filename': 'error.log',
            'mode': 'w',
            'formatter': 'formatter1',
            'filters': ['error_filter']
        },
        'critical_file': {
            'class': logging.FileHandler,
            'filename': 'critical.log',
            'mode': 'w',
            'formatter': 'formatter3',
            'filters': ['critical_filter']
        }

    },
    'loggers': {
        'module1': {
            'level': 'DEBUG',
            'handlers': ['error_file']
        },
        'module2': {
            'handlers': ['stdout']
        },
        'module3': {
            'handlers': ['stderr', 'critical_file']
        }
    },
    'root': {
        'formatter': 'default',
        'handlers': ['default']
    }
}