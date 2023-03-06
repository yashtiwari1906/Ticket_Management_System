from rest_framework import routers
from django.urls import path , include
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('reset/', views.ResetDataBase().reset, name ='reset'),
]