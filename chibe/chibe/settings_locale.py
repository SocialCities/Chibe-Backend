import os 

DEBUG = True
CORS_ORIGIN_ALLOW_ALL = True
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATICFILES_DIRS = [
	'/Users/riccardo/Desktop/chibe/chibe/static',
]

MEDIA_ROOT = "/Users/riccardo/Desktop/chibe/chibe/media" 
STATIC_ROOT = "/Users/riccardo/Desktop/chibe/chibe/static"

LOGGING = {
	'version': 1,
	'formatters': {
		'verbose': {
			'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
		},
		'simple': {
			'format': '%(levelname)s %(message)s'
		},
	},
	'filters': {
		'special': {
			'()': 'django.utils.log.RequireDebugFalse',
		},
	},
	'handlers': {
		'console': {
			'level': 'DEBUG',
			'class': 'logging.StreamHandler',
			'formatter': 'verbose'
		},
		'debug_file': {
			'level': 'DEBUG',
			'class': 'logging.FileHandler',
			'filename': '/Users/riccardo/Desktop/chibe/chibe/logs/debug.log',
			'formatter': 'verbose'
		},
		'error_file': {
			'level': 'ERROR',
			'class': 'logging.FileHandler',
			'filename': '/Users/riccardo/Desktop/chibe/chibe/logs/error.log',
			'formatter': 'verbose'
		},
	},
	'loggers': {
		'django': {
			'handlers': ['debug_file', 'error_file'],
			'level': 'DEBUG',
			'propagate': True,
		},
	}
}