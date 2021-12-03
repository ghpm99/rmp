from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='web'),
    path('youtube/', views.youtube, name='youtube'),
    path('navigation/', views.navigation, name='navigation')
]
