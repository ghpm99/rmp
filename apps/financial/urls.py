from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_view, name='financial_get_all'),
    path('new-payment', views.save_new_view, name='financial_save_new'),
]
