from django.db import models

# Create your models here.

class Booking(models.Model):
    ticket = models.CharField(max_length = 50)
    event = models.CharField(max_length=250)
    user_id = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.ticket


class Seats(models.Model):
    event = models.CharField(max_length = 50) 
    row = models.IntegerField()
    col = models.IntegerField() 
    booked = models.BooleanField() 

    def __str__(self): 
        return self.event + "_" + "(" + str(self.row) +"," + str(self.col) + ")"