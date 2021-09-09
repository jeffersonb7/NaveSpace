from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.site_institucional.urls')),
    path('admin/', admin.site.urls),
]
