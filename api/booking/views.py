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
    #seat is class attribute not instance attribute, faced some bugs when declaring it in __init__ cancel function was unable to update it
    seats = {}
    def __init__(self): 
        self.userOperations = UserOperations()
        self.booking = Booking #for fetching details of ticket at the last to throw json response
        
        
    def returnTicketName(self, row, col, event): 
        if event not in self.seats: 
            self.seats[event] = [[False for _ in range(15)] for _ in range(10)]
            
        if self.seats[event][row][col]: 
            return [False, {"sold_out":False, "msg": "seat is booked, book other"}]

        self.seats[event][row][col] = True 
        

        #grabing ticket info from tickets left or booked 
        
        eo = EventOperations() 
        tickets_booked = eo.getBookedTickets(event = event) 

        if tickets_booked==150: 
            return [False, {"sold_out":True, "error":"Tickets are not available"}]
        tickets_booked+=1 

        #ticket 
        ticket = event + "_" +"R"+str(row)+"C"+str(col)

        #updating info of tickets availability 
        eo.changeTickets(event, ticket_left = 150 - tickets_booked, ticket_booked = tickets_booked)

        return [True, {"sold_out":False, "ticket": ticket}]

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
        
        self.seats[event][row][col] = False
        

        #delete from Booking model
        self.booking.objects.filter(ticket = ticket).delete() 
        
        #grabing ticket info from tickets left or booked 
        eo = EventOperations() 
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
        #row = int(request.POST['row'])
        #col = int(request.POST['col'])
        event_dict = request.POST["event_dict"]  # {"event":[(), (), ()], .....}
        event_dict = json.loads(event_dict)
        #event 
        #event = request.POST['event']
        
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

        #checking wether ticket is available 
        

        #pass to processEvents to book ticket
        # response_return_ticket = self.returnTicketName(row, col, event)
        # if not response_return_ticket[0]: #so ticket can't be booked
        #     return response_return_ticket[1] 

        # ticket = response_return_ticket[1]["ticket"]

        # response_ticket_save = self.saveTicketDetails(ticket, event, user_id)
        # return response_ticket_save

        response_for_process = self.processEvents(event_dict, user_id)
        return response_for_process
    
    def processEvents(self, event_dict, user_id): 
        # {"event":[(), (), ()], .....}
        #o/p - > {"event_name":"", "tickets":[], "seatsNotBooked":[], "msg":"reason for not booking of seats"}
        #not_available_seats, booked_tickets = [], []
        result_for_processEvents = {}
        for event_name, seat_list_str in event_dict.items(): 
            
            seat_list = [(int(seat[1]), int(seat[4])) for seat in seat_list_str.split(":")]
            num_tickets = len(seat_list)
            not_available_seats, booked_tickets = [], []
            tickets, seatsNotAvailable, msg = [], [], ""
            for i, seat in enumerate(seat_list): 
                #event_name, seat(r, c)
                row, col = seat 
                response_return_ticket = self.returnTicketName(row, col, event_name)
                if not response_return_ticket[0]: #so ticket can't be booked
                    print(response_return_ticket)
                    if response_return_ticket[1]["sold_out"]:
                        not_available_seats.extend(seat_list[i:])
                        seatsNotAvailable = not_available_seats.copy() 
                        tickets = booked_tickets.copy()
                        msg = "Tickets has been completely sold out"
                        break
                    else:
                        not_available_seats.append(tuple(seat))
                       
                else:
                    ticket = response_return_ticket[1]["ticket"]
                    booked_tickets.append(ticket)
                    response_ticket_save = self.saveTicketDetails(ticket, event_name, user_id)
            print("*"*20)
            if msg == "":
                tickets = booked_tickets.copy() 
                seatsNotAvailable = tuple(not_available_seats.copy())
                if len(seatsNotAvailable) == 0: 
                    msg = "All seats has been booked successfully"
                else:
                    msg = "seats were already booked"

                response_process_event = {
                    "event_name":event_name,
                    "booked_tickets": tickets,
                    "seats_not_booked": seatsNotAvailable,
                    "msg":msg  
                }

            else: 
                response_process_event = {
                    "event_name":event_name,
                    "booked_tickets": tickets,
                    "seats_not_booked": seatsNotAvailable,
                    "msg":msg  
                }
            result_for_processEvents[event_name] = response_process_event
        return JsonResponse(result_for_processEvents)


    def saveTicketDetails(self, ticket, event, user_id):

        tickets_info = Booking(ticket = ticket, event = event, user_id = user_id)
        tickets_info.save() 
        ticket_dict = self.booking.objects.filter(user_id = user_id).values().last() 
        #ticket_dict["ticket"] = ticket
        return {"details": ticket_dict}  




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


class CancelBookedTicket(): 
    def __init__(self): 
        self.booking = Booking()
        

    def cancelAll(self, request):
        if not request.method == 'POST':
            return JsonResponse({'error': 'Send a post request with a single ticket as parameter'}) 
        
        ticket = request.POST["ticket"] 
        user_dict = self.booking.objects.filter(ticket = ticket).values() 
        
        #checking valid user_id
        if not user_dict.exists():
            return JsonResponse({"error":True, "msg": "send a valid ticket"}) 
        
        event = user_dict.first()['event']
        #delete from Booking model
        self.booking.objects.filter(ticket = ticket).delete() 



    

        
        

