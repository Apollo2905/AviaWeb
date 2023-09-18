from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *  # импортирование модели

from datetime import datetime


def home(request):
    departure = request.GET.get('departure')
    arrival = request.GET.get('arrival')
    scheduled_departure = request.GET.get('scheduled_departure')
    # scheduled_arrival = request.GET.get('scheduled_arrival')
    flights = Flight.objects.all()
    if departure or arrival or scheduled_departure:
        flights = Flight.objects.filter(
            Q(departure_airport__city__icontains=departure) |
            Q(arrival_airport__city__icontains=arrival) |
            Q(scheduled_departure__date__icontains=arrival)
            # Q(scheduled_arrival__date__icontains=arrival)
        )[:10]
        print(flights)
        for fl in flights:
            # { %for pass in flight.ticketflight_set.all %}
            #     < button > {{ticketflight}} < / button >
            # { % endfor %}
            for pas in fl.ticketflight_set.all():
                print(pas.ticket_no)
        return render(request, 'flights.html', {'flights': flights})
    return render(request, 'home.html', {})

