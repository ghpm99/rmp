from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='web'),
    path('youtube/', include([
        path('', views.youtube, name='youtube'),
        path('change-screen', views.change_screen, name='api_youtube')
    ])),
    path('navigation/', views.navigation, name='navigation'),
]
