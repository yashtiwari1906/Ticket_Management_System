from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
import json
from django.contrib.auth import authenticate
import sys
from .models import ResetInfo
#since we can not dorectly import from parent directory
sys.path.append('..')

# importing
from api.user.models import User
from  api.event.models import Event 
from  api.booking.models import Booking, Seats



class ResetDataBase(): 
    def __init__(self): 
        self.user = User 
        self.event = Event  
        self.booking = Booking
        self.seats = Seats

    def resetUserModel(self): 
        self.user.objects.all().delete() 
        return JsonResponse({"success":True, "msg": "All users has been deleted"})

    def resetEventModel(self): 
        queryset = self.event.objects.all().values()
    
        for query in queryset: 
            event = query["event_name"]
            info = self.event.objects.get(event_name = event)
            info.tickets_booked = 0
            info.tickets_left= 150
            info.save()
        return JsonResponse({"success":True, "msg": "All events tickets has been reset"})

    def resetBookingModel(self): 
        self.booking.objects.all().delete() 
        self.seats.objects.all().delete() 
        return JsonResponse({"success":True, "msg": "All bookings has been cancelled"})

    @csrf_exempt
    def reset(self, request): 
        if not request.method == 'POST':
            return JsonResponse({'error': 'Send a post request with valid paramenter only'}) 

        username = request.POST['username']
        password = request.POST['password']

        #superuser_queryset = AuthUser.objects.filter(is_superuser=True)
        #superuser = superuser_queryset.values().first()
        
        if authenticate(username = username, password = password) is not None: 
            User.objects.all().delete()
            self.resetEventModel() 
            self.resetUserModel()
            self.resetBookingModel()

            #saving reset Info
            resetinfo = ResetInfo(username = username)
            resetinfo.save()

            return JsonResponse({'success':True,'error':False,'msg':'Data Base has been reset successfully'}) 
        else: 
            return JsonResponse({'success':False,'error':True,'msg':'Please provide right credentials for admin'}) 

@csrf_exempt 
def home(request): 
    return JsonResponse({"msg": "It's an Admin reset API, please hit resetApi/reset/ with valid credentials"})
