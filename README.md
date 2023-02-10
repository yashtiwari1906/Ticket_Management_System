# Ticket_Management_System

## Create SuperUser 
    `python manage.py createsuperuser` 
    
    - Fill Username and password  
    - If don't wan't to create a superuser use 
      * username = arya
      * password = Arya@123
    
## Installation 

 ### Install all requirements from requirements.txt 
      `pip install -r requirements.txt`
      
 ### Make all Migrations & Migrate (Good Practice) 
    `python manage.py makemigrations`
    `python manage.py migrate`
    
### Run the django app 
    ` python manage.py runserver ` 
    
### URLS fr the project
    * Majorly we'll need admin url to access admin panel from web which is http://127.0.0.1:8000/admin/ and rest all urls are on postman link to workspace is given below.
    * https://app.getpostman.com/join-team?invite_code=381ad60225f2f9b40ee9349f40e99442&target_code=0a3d1cb55f54a0e4e3b2bae9e022319e
    
### prequisites 
    * Once the server is live login to admin by hiting the url http://127.0.0.1:8000/admin/ and add the Events of your choice say. comedy_show, movie, etc. and then you can go ahead with testing it out for those events.
    * PS. I have only considered 150 seats.
    
### Future Work 
    * starting booking time is more because system is generating all the corresponding tickets, It can be improved by generating tickets at the time of event registry.
    * User login/logout functionality based on JWT can be introduced so that updation of details don't require old details.
    * Responses are not very standard they can be standardized with respect to the inputs from Frontend.
    
    
  
