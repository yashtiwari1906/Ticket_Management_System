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
      
 ### Make all Migrations & Migrate (Good Practise) 
    `python manage.py makemigrations`
    `python manage.py migrate`
    
### Run the django app 
    `python manage.py runserver`
### Some Important Info 
    * The main branch has all the must have points of the doc provided. 
    * branch name feature/book-multiple-events is the implementation of the good to have points of the doc.
    
### Future Work 
    * starting booking time is more because system is generating all the corresponding tickets, It can be improved by generating tickets at the time of event registry.
    * User login/logout functionality based on JWT can be introduced so that updation of details don't require old details.
    * Responses are not very standard they can be standardized with respect to the inputs from Frontend.
    
    
  
