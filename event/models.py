from django.db import models

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=30)
    date_of_event = models.DateField()
    description = models.TextField()
    venue = models.CharField(max_length=30)
    start_of_event = models.DateField()
    end_of_event = models.DateField()
    
    def __str__(self):
        return self.event_name