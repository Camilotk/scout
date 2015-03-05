#!/usr/bin/python
import os
import sys

# sys.path.append('/work/scout')
#os.environ['PYTHON_EGG_CACHE'] = '/work/cache/.python-egg'
sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'scout'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'scout.settings'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

#import os
#import sys
#from django.core.wsgi import get_wsgi_application

#sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'scout'))
#os.environ['DJANGO_SETTINGS_MODULE'] = 'scout.settings'

#application = get_wsgi_application()