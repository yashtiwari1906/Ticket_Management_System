from rest_framework import viewsets 
from django.shortcuts import render
from django.http import JsonResponse
from .serializers import EventSerializers
from .models import Event
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
import json
# Create your views here.
 
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('event_id')
    
    serializer_class = EventSerializers


#This is for if just we have to show numbers not original tickets
class EventOperations():  
    def __init__(self):
        pass

    def getAvailableTickets(self, event): 
        event_dict = Event.objects.all().filter(event_name = event).values().first()
        return int(event_dict["tickets_left"])

    def getBookedTickets(self, event): 
        event_dict = Event.objects.all().filter(event_name = event).values().first()
        return int(event_dict["tickets_booked"])

    def changeTickets(self, event, ticket_left, ticket_booked): 
        self.info = Event.objects.get(event_name = event)
        self.info.tickets_left = ticket_left 
        self.info.save()

        self.info = Event.objects.get(event_name = event)
        self.info.tickets_booked = ticket_booked
        self.info.save()

    
    #reset tickets 
    def reset(self): 
        queryset = Event.objects.all() 

        for query in queryset: 
            query["tickets_booked"] = 0 
            query["tickets_left"] = 150

            query.save()
        print("reset complete!!")

    @csrf_exempt
    def ticketInfo(self, request): 
        if not request.method == 'POST':
            return JsonResponse({'error': 'Send a post request with a single event as parameter'}) 
        
        event = request.POST["event"] 

        tickets_left = self.getAvailableTickets(event)
        tickets_booked = self.getBookedTickets(event) 

        return JsonResponse({'success':True, 'event':event, 'tickets_booked': tickets_booked, 'tickets_left':tickets_left})



    


