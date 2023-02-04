from rest_framework import viewsets 
from .serializers import BookingSerializers
from .models import Booking
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
import json
from ..user.views import UserOperations
from  ..event.views import EventOperations
# Create your views here.
 
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('ticket')
    serializer_class = BookingSerializers

class BookingOperations(): 
    def __init__(self): 
        self.userOperations = UserOperations()
        self.booking = Booking #for fetching details of ticket at the last to throw json response
        


    @csrf_exempt
    def book(self, request): 
        if not request.method == 'POST':
            return JsonResponse({'error': 'Send a post request with valid paramenter only'})
        
        name = request.POST.get('name', "Anonmous")
        email = request.POST['email']
        contact = request.POST['contact']
        
        #event 
        event = request.POST['event']

        if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email):
            return JsonResponse({'error': 'Enter a valid email'})
        
        response = self.userOperations.checkUserExists(request) 
        response = json.loads(response.content.decode('utf-8'))
       
        if response["exists"]:
            user_id = response["id"]
        else: 
            response_user_creation = self.userOperations.signin(request)
            response_user_creation = json.loads(response_user_creation.content.decode('utf-8'))
            user_details= response_user_creation["details"]
            user_id = user_details["id"]

        #grabing ticket info from tickets left or booked 
        eo = EventOperations(event = event) 
        tickets_booked = eo.getBookedTickets() 

        if tickets_booked==150: 
            return JsonResponse({"error":"Tickets are not available"}) 
        print(tickets_booked, type(tickets_booked))
        tickets_booked+=1 

        #ticket 
        ticket = event + "_" +str(tickets_booked) 

        #updating info of tickets availability 
        eo.changeTickets(event, ticket_left = 150 - tickets_booked, ticket_booked = tickets_booked)

        response_ticket_save = self.saveTicketDetails(ticket, event, user_id)
        return response_ticket_save

    def saveTicketDetails(self, ticket, event, user_id):

        tickets_info = Booking(ticket = ticket, event = event, user_id = user_id)
        tickets_info.save() 
        ticket_dict = self.booking.objects.filter(user_id = user_id).values().first()
        return JsonResponse({'success':True,'error':False,'msg':'user saved successfully', "details": ticket_dict})  




