import os
import sys
import site

from os.path import dirname, abspath, join

PROJECT_DIR = dirname(abspath(join(__file__, '..')))
BASE_DIR = dirname(abspath(join(__file__, '..', '..')))

sys.path.insert(0, PROJECT_DIR)
sys.path.insert(1, BASE_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

site.addsitedir('/home/sserrano/env/lib/python2.6/site-packages')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

