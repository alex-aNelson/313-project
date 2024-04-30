from django.db import models
from django.contrib.auth.models import User # Import built in User model

# Create your models here.
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    event_date = models.DateTimeField()
    users_event = models.ForeignKey(User, on_delete=models.CASCADE) # Each event is associated with one user

    def __str__(self):
        return self.title
