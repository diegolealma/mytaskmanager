# project_root/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('tasks.urls')),  # Inclui as URLs do app task
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'),
]
