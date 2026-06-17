from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chronicles/', views.chronicles_archive, name='chronicles_archive'), # New!
    path('post/<int:pk>/', views.chronicle_detail, name='chronicle_detail'),
    # New Static Pages
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('machines/', views.machines, name='machines'),
]

