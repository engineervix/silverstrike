from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView  # noqa: F401

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    url(r'', include('silverstrike.urls')),
]
