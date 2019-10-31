from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('wedding/', include('wedding.urls')),
    path('admin/', admin.site.urls),
]
