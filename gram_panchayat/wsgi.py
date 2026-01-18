"""
WSGI config for gram_panchayat project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gram_panchayat.settings')

application = get_wsgi_application()
