"""
Definition of urls for Application.
"""

from django.urls import include,path
from django.contrib import admin


urlpatterns = [
    path('',include('accounts.urls')),
    path('',include('Esgb.urls')),
    path('admin/', admin.site.urls),
]
