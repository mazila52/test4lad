from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('library.urls', namespace='library')),
]
