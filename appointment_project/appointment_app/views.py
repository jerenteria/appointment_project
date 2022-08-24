from django.shortcuts import render, redirect
from .models import *


def index(request):
    context = {
        'all_appointments': Appointment.objects.all()
    }
    return render(request, "index.html", context)

def create_appointment(request):
    Appointment.objects.create(
        day = request.POST['day'],
        notes = request.POST['notes']
    )
    return redirect("/")

