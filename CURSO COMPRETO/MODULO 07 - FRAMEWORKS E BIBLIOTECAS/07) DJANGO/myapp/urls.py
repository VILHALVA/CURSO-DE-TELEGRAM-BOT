from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save_settings/', views.save_settings, name='save_settings'),
]
