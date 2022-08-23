from django.db import models

class Appointment(models.Model):
    day = models.DateTimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    notes = models.TextField(blank=True, null=True)
