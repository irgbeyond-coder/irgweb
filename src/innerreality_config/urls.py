from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Check this line: it should be 'site.urls' not 'site.py'
    path('', include('core.urls')), # Points to the OTHER file
]
