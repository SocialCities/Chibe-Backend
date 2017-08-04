import os 

DEBUG = True
CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2', 
		'NAME': 'django', 
		'USER': 'django',
		'PASSWORD': 'c7a874074681c888a19764bd4ff4b916',
		'HOST': 'localhost',
		'PORT': '', 
	}
}

MEDIA_ROOT = "/home/django/media" 
STATIC_ROOT = "/home/django/static"

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
		'null': {
			'level': 'ERROR',
			'class': 'logging.NullHandler',
		},	
		'console': {
			'level': 'DEBUG',
			'class': 'logging.StreamHandler',
			'formatter': 'verbose'
		},
		# 'mail_admins': {
		# 	'level': 'ERROR',
		# 	'class': 'django.utils.log.AdminEmailHandler',
		# 	'include_html': True,
		# 	'filters': ['special']
		# },
		'debug_file': {
			'level': 'DEBUG',
			'class': 'logging.FileHandler',
			'filename': '/home/django/logs/debug.log',
			'formatter': 'verbose'
		},
		'error_file': {
			'level': 'ERROR',
			'class': 'logging.FileHandler',
			'filename': '/home/django/logs/error.log',
			'formatter': 'verbose'
		},	
	},
	'loggers': {
		'django.security.DisallowedHost': {
			'handlers': ['null'],
			'propagate': False,
		},
		'django.request': {
			'handlers': ['debug_file', 'error_file'],
			'level': 'DEBUG',
			'propagate': True,
		},	
	}
}