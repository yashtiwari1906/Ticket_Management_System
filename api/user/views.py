from rest_framework import viewsets 
from .serializers import UserSerializers
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
#from django.contrib.auth.models import User as AuthUser
from django.contrib.auth import authenticate

# Create your views here.
 
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializers


class UserOperations():
    def __init__(self):
        self.name = "user"

    @csrf_exempt
    def checkUserExists(self, request): 
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']

        try:
            query = User.objects.filter(email = email).filter(name = name).filter(contact = contact)
            if query.exists(): 
                return JsonResponse({"exists":True, "id":query.values().first()["id"]})
            else:
                return JsonResponse({"exists":False})
        except: 
            return JsonResponse({"exists":False, "error":"some error happened while checking in model"})



    
    @csrf_exempt 
    def signin(self, request): 

        if not request.method == 'POST':
            return JsonResponse({'error': 'Send a post request with valid paramenter only'})

        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']

        if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email):
            return JsonResponse({'error': 'Enter a valid email'})

        

        user = User(name = name, email = email, contact = contact)
        user.save() 
        usr_dict = User.objects.filter(email = email).values().first()
        return JsonResponse({'success':True,'error':False,'msg':'user saved successfully', "details": usr_dict}) 

    @csrf_exempt
    def update(self, request, id):
        if not request.method == 'POST':
            return JsonResponse({'error': 'Send a post request with valid paramenter only'}) 

        updated_name = request.POST['name']
        updated_email = request.POST['email']
        updated_contact = request.POST['contact'] 

        user = User.objects.get(id = id)
        user.name = updated_name 
        user.email = updated_email 
        user.contact = updated_contact 
        user.save()
        usr_dict = User.objects.filter(id = id).values().first()
        return JsonResponse({'success':True,'error':False,'msg':'user details updated successfully', "details": usr_dict}) 

    @csrf_exempt
    def details(self, request, id): 
        usr_dict = User.objects.filter(id = id).values().first() 
        new_usr_dict = {k:v for k, v in usr_dict.items() if k in ["name", "email", "contact"]}
        return JsonResponse({'success':True,'error':False,'msg':'user details fetched successfully', "details": new_usr_dict}) 



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
            return JsonResponse({'success':True,'error':False,'msg':'Data Base has been reset successfully'}) 
        else: 
            return JsonResponse({'success':False,'error':True,'msg':'Please provide right credentials for admin'}) 








    