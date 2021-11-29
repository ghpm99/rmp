from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='routines'),
    path('kanban/', views.kanban, name='kanban'),
    path('financial/', views.financial, name='financial')
]
