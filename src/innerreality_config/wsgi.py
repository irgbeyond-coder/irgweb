import os
from django.core.wsgi import get_wsgi_application

# We tell Django where your settings are located
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'innerreality_config.settings')

application = get_wsgi_application()