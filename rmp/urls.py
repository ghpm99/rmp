from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pusher/', include('pusher_webhook.urls')),
    path('remote/', include('remote.urls')),
    path('auth/', include('authentication.urls')),
]
