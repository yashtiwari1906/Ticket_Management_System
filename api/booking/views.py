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
        
        name = request.POST['name']
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
        eo = EventOperations() 
        tickets_booked = eo.getBookedTickets(event = event) 

        if tickets_booked==150: 
            return JsonResponse({"error":"Tickets are not available"}) 
    
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
        ticket_dict = self.booking.objects.filter(user_id = user_id).values().last() 
        #ticket_dict["ticket"] = ticket
        return JsonResponse({'success':True,'error':False,'msg':'user saved successfully', "details": ticket_dict})  




class RetrievingOperations():
    def __init__(self):
        self.userOperations = UserOperations()
        self.booking = Booking #for fetching details of ticket at the last to throw json response

    @csrf_exempt
    def viewTicketsByUser(self, request): 
        if not request.method == 'POST':
            return JsonResponse({'error': 'Send a post request with a single user_id as parameter'}) 

        user_id = request.POST["user_id"] 
        
        user_dict = self.booking.objects.filter(user_id = user_id).values() 
        
        #checking valid user_id
        if not user_dict.exists():
            return JsonResponse({"error":True, "msg": "send a valid user_id"})
        

        ticket_list = []
        for user in user_dict: 
            ticket_list.append(user['ticket']) 

        return JsonResponse({'success': True, 'tickets': ticket_list})

    @csrf_exempt 
    def viewUserDetailsFromTicket(self, request):
        if not request.method == 'POST':
            return JsonResponse({'error': 'Send a post request with a single ticket as parameter'}) 
        
        ticket = request.POST["ticket"] 
        
        user_dict = self.booking.objects.filter(ticket = ticket).values() 
        
        #checking valid user_id
        if not user_dict.exists():
            return JsonResponse({"error":True, "msg": "send a valid ticket"}) 
        print(user_dict.first())
        user_id = user_dict.first()['user_id']
        response_details = self.userOperations.details(user_id)

        return response_details

    

        
        

