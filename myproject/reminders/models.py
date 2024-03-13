from django.db import models

# Create your models here.

class Reminder(models.Model):
    date_and_time = models.DateTimeField()
    message = models.TextField()