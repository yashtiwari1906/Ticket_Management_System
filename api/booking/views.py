from rest_framework import viewsets 
from .serializers import BookingSerializers
from .models import Booking, Seats
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
import json
from ..user.views import UserOperations
from  ..event.views import EventOperations
from ..event.models import Event
# Create your views here.
 
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('ticket')
    serializer_class = BookingSerializers

class BookingOperations(): 
    def __init__(self): 
        self.userOperations = UserOperations()
        self.eventoperations = EventOperations()
    
        self.booking = Booking #for fetching details of ticket at the last to throw json response
        self.events = Event.objects.values_list("event_name", flat = True).order_by("event_name") #comparing user entered a valid event or not
        self.seats = Seats #for handling seats booking and cancellation
        
        
    def returnTicketName(self, row, col, event): 
        query = self.seats.objects.filter(event = event).values()
        if not query.exists(): 
            #filling model Seats with default values 
            for i in range(1, 10+1): 
                for j in range(1, 15+1): 
                    seat_instance = self.seats(event = event, row = i, col = j, booked = False)
                    seat_instance.save() 

        #grabing ticket info from tickets left or booked 
        eo = self.eventoperations 
        tickets_booked = eo.getBookedTickets(event = event) 

        if tickets_booked==150: 
            return [False, JsonResponse({"error":"Tickets are not available"})]

        query = self.seats.objects.filter(event = event).filter(row = row).filter(col = col).filter(booked = True).values()
        if query.exists(): 
            return [False, JsonResponse({"msg": "seat is booked, book other"})]

        #booking seat for (row, col)
        self.seats.objects.filter(event = event).filter(row = row).filter(col = col).update(booked = True)

        tickets_booked+=1 

        #generating ticket 
        ticket = event + "_" +"R"+str(row)+"C"+str(col)

        #updating info of tickets availability 
        eo.changeTickets(event, ticket_left = 150 - tickets_booked, ticket_booked = tickets_booked)

        return [True, {"ticket": ticket}]

    @csrf_exempt
    def cancel(self, request):
        if not request.method == 'POST':
            return JsonResponse({'error': 'Send a post request with a single ticket as parameter'}) 
        
        ticket = request.POST["ticket"] 
        user_dict = self.booking.objects.filter(ticket = ticket).values() 
        
        #checking valid user_id
        if not user_dict.exists():
            return JsonResponse({"error":True, "msg": "send a valid ticket"}) 
        
        event = user_dict.first()['event']
        
        #free up the seat 
        for i, char in enumerate(ticket): 
            if char == "R":
                row = int(ticket[i+1])
            if char == "C": 
                col = int(ticket[i+1])
        #making seat available at (row, col)
        self.seats.objects.filter(event = event).filter(row = row).filter(col = col).update(booked = False)
        
    
        #delete from Booking model
        self.booking.objects.filter(ticket = ticket).delete() 
        
        #grabing ticket info from tickets left or booked 
        eo = self.eventoperations
        tickets_booked = eo.getBookedTickets(event = event) 
    
        tickets_booked-=1 

        #updating info of tickets availability 
        eo.changeTickets(event, ticket_left = 150 - tickets_booked, ticket_booked = tickets_booked)

        return JsonResponse({"success":True, "msg":f"ticket {ticket} deleted successfully.."})


    @csrf_exempt
    def book(self, request): 
        if not request.method == 'POST':
            return JsonResponse({'error': 'Send a post request with valid paramenter only'})
        
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        row = int(request.POST['row'])
        col = int(request.POST['col'])
        #event 
        event = request.POST['event']

        if event not in self.events: 
            return JsonResponse({"success":False, "msg": "Enter a valid event name"})
    
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

        response_return_ticket = self.returnTicketName(row, col, event)
        if not response_return_ticket[0]: #so ticket can't be booked
            return response_return_ticket[1] 

        ticket = response_return_ticket[1]["ticket"]

        response_ticket_save = self.saveTicketDetails(ticket, event, user_id)
        return response_ticket_save

    def saveTicketDetails(self, ticket, event, user_id):

        tickets_info = Booking(ticket = ticket, event = event, user_id = user_id)
        tickets_info.save() 
        ticket_dict = self.booking.objects.filter(user_id = user_id).values().last() 
        
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
            return JsonResponse({"error":True, "msg": "send a valid user_id or there has been no tickets booked by this user"})
        

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
    
        user_id = user_dict.first()['user_id']
        response_details = self.userOperations.details(user_id)

        return response_details


