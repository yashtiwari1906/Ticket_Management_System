from rest_framework import viewsets 
from django.shortcuts import render
from django.http import JsonResponse
from .serializers import EventSerializers
from .models import Event
# Create your views here.
 
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('event_id')
    
    serializer_class = EventSerializers


#This is for if just we have to show numbers not original tickets
class EventOperations():  
    def __init__(self, event):
        self.event = event 
        self.data = Event.objects.all().filter(event_name = self.event).values().first()

    def getAvailableTickets(self): 
        return int(self.data["tickets_left"])

    def getBookedTickets(self): 
        return int(self.data["tickets_booked"])

    def changeTickets(self, event, ticket_left, ticket_booked): 
        self.info = Event.objects.get(event_name = self.event)
        self.info.tickets_left = ticket_left 
        self.info.save()

        self.info = Event.objects.get(event_name = self.event)
        self.info.tickets_booked = ticket_booked
        self.info.save()

    
    #reset tickets 
    def reset(self): 
        queryset = Event.objects.all() 

        for query in queryset: 
            query["tickets_booked"] = 0 
            query["tickets_left"] = 0 

            query.save()
        print("reset complete!!")


    


