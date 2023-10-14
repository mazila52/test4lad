from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.urls.conf import include

from . import settings

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('library.urls', namespace='library')),
]

# If DEBUG, can see cover's images in MEDIA
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
