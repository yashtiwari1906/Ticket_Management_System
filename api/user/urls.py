from rest_framework import routers
from django.urls import path , include
from . import views


router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [
    path('signin/',views.UserOperations().signin, name ='signin'),
    path('update/', views.UserOperations().update, name ='update'),
    path('details/', views.UserOperations().details, name ='details'),
    path('reset/', views.UserOperations().reset, name ='reset'),
    path('check/', views.UserOperations().checkUserExists, name ='check'),
    path('', include(router.urls)),
    
]

