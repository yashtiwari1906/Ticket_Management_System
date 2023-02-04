from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length = 50)
    event_id = models.CharField(max_length = 50)
    tickets_booked = models.IntegerField()
    tickets_left = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.event_name