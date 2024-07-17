from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', index, name="index"),
    path('a-propos/', About, name="about"),
    path('status/', status, name="status")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)