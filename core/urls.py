# core/urls.py

from django.contrib import admin
from django.urls import path, include
from maps_api.views import home_view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('api/', include('maps_api.urls')),
]