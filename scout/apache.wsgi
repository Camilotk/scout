# -*- coding:utf-8 -*-
import os
import sys

sys.path.append('/work/scout')

os.environ['PYTHON_EGG_CACHE'] = '/work/cache/.python-egg'
os.environ['DJANGO_SETTINGS_MODULE'] = 'scout.settings'

#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
