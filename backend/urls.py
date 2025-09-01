from django.contrib import admin
from django.urls import path, include
from stapp.server_time import server_time
from django.conf import settings
from django.conf.urls.static import static



# Also add API prefix to stapp URLs
urlpatterns = [
    path('aarizmaan/', admin.site.urls),
    path('api/', include('stapp.urls')),
    path('api/server-time/', server_time, name='server_time'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

