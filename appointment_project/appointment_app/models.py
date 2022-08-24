from django.db import models
from datetime import datetime

class Appointment(models.Model):
    day = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
