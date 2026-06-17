import os
from django.core.asgi import get_asgi_application

# Again, pointing to your specific website folder's settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'innerreality_config.settings')

application = get_asgi_application()
