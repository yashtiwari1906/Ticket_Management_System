from rest_framework import routers
from django.urls import path , include
from . import views


router = routers.DefaultRouter()
router.register(r'', views.BookingViewSet)

urlpatterns = [
    path('book/',views.BookingOperations().book, name ='book'),
    path('', include(router.urls))
]