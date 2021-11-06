from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.catchall),
    path('media/', include('media.urls')),
    path('admin/', admin.site.urls),
]
