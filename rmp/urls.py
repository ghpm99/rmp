from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('media/', include('media.urls')),
    path('web/', include('web.urls')),
    path('routines/', include('routines.urls')),
    path('server/', include('server.urls')),
    path('status/', include('status.urls')),
    path('admin/', admin.site.urls),
    path('socket/', include('media_socket.urls')),
]
