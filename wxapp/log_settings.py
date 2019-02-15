#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "chenwei"
# Date: 2019/2/15

import os

LOG_DIR = '/data/log/wxapp/app/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'profile': {
            'format': '%(asctime)s %(message)s'
        },
        'consumer': {
            'format': '%(asctime)s %(levelname)s Process ID:%(process)d %(module)s.%(funcName)s Line:%(lineno)d %(message)s'
        },
        'raw': {
            'format': '%(message)s'
        },
    },

    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'default.log'),
            'formatter': 'verbose',
        },
        'info_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'info.log'),
            'formatter': 'verbose',
        },
        'error_handler': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'formatter': 'verbose',
        },
        'profile_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'profile.log'),
            'formatter': 'profile',
            'maxBytes': 500 * 1024 * 1024,  # 500M
        },

        'exception_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'exception.log'),
            'formatter': 'verbose',
        },

        'tracer_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'tracer.log'),
            'formatter': 'raw',
        },

        'auth_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'auth.log'),
            'formatter': 'verbose',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 30,
        },
        'wechat_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'wechat.log'),
            'formatter': 'verbose',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 30,
        },
        'rpc_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'rpc_logger.log'),
            'formatter': 'verbose',
        },
    },

    'loggers': {
        'django': {
            'handlers': ['default'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['error_handler'],
            'level': 'ERROR',
            'propagate': False,
        },
        'info_logger': {
            'handlers': ['info_handler', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'error_logger': {
            'handlers': ['error_handler'],
            'level': 'ERROR',
            'propagate': False,
        },
        'profile_logger': {
            'handlers': ['profile_handler'],
            'level': 'INFO',
            'propagate': False,
        },

        'exception_logger': {
            'handlers': ['exception_handler'],
            'level': 'ERROR',
            'propagate': False,
        },

        'gm_tracer.subscribe': {
            'handlers': ['tracer_handler'],
            'propagate': False,
            'level': 'INFO'
        },

        'auth_logger': {
            'handlers': ['auth_handler'],
            'propagate': False,
            'level': 'INFO'
        },
        'wechat_logger': {
            'handlers': ['wechat_handler'],
            'propagate': False,
            'level': 'INFO'
        },
        'rpc_logger': {
            'handlers': ['rpc_handler'],
            'propagate': False,
            'level': 'INFO'
        },
    }
}




