from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER' :'luismartin',
        'PASSWORD': 'luismartincursopro',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/empleado/static/'
# STATIC_URL = 'empleado/empleado/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'  
MEDIA_ROOT = BASE_DIR.child('media')

# # Default primary key field type
# # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




# #añadido en base al consejo del profesor de udemy con codligo github lecc 22

# STATICFILES_DIRS = [BASE_DIR.child('static')]

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR.child('media')
