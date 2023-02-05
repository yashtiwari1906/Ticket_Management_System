from rest_framework import routers
from django.urls import path , include
from . import views


router = routers.DefaultRouter()
router.register(r'', views.BookingViewSet)

urlpatterns = [
    path('book/',views.BookingOperations().book, name ='book'),
    path('tickets/',views.RetrievingOperations().viewTicketsByUser, name ='tikcetsByUser'),
    path('userdetails/',views.RetrievingOperations().viewUserDetailsFromTicket, name ='userInfo'),
    path('cancel/',views.BookingOperations().cancel, name ='cancel'),
    path('', include(router.urls))
]

