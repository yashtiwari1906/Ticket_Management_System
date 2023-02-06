# Ticket_Management_System

## Create SuperUser 
    ```python manage.py createsuperuser``` 
    
    - Fill Username and password  
    - If don't wan't to create a superuser use 
      * username = arya
      * password = Arya@123
    
## Installation 

 ### Install all requirements from requirements.txt 
      ``` pip install -r requirements.txt ```
      
 ### Make all Migrations & Migrate (Good Practise) 
    ```python manage.py makemigrations```
    ```python manage.py migrate```
    
### Run the django app 
    ```python manage.py runserver```

### Future Work 
    * starting booking time is more because system is generating all the corresponding tickets, It can be improved by generating tickets at the time of event registry.
    * User login/logout functionality based on JWT can be introduced so that updation of details don't require old details
    
    
  
