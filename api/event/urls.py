from rest_framework import routers
from django.urls import path , include
from . import views


router = routers.DefaultRouter()
router.register(r'', views.EventViewSet)


    
urlpatterns = [
    path('eventinfo/',views.EventOperations().ticketInfo, name ='ticketInfo'),
    path('', include(router.urls)),
]