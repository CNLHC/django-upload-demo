import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY = '(e$z03ckbeb^9b%)4m&l+bnm&cvsml4@-m17$tydwny9iyzvko'
DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [ 'filemanage' ]
ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
MEDIA_ROOT = BASE_DIR+'/media/'
STATIC_ROOT =   BASE_DIR+"/static"
STATIC_URL = '/static/'


