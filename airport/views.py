from django.http import HttpResponse
from django.template import loader

from airport.models import Airport, Flight

def airports_view(request):
    airports = Airport.objects.all()
    content = {
        'airports': airports
    }
    template = loader.get_template('airport/airports.html')
    return HttpResponse(template.render(content, request))

def airport_detail_view(request, pk):
    airport = Airport.objects.get(pk=pk)
    content = {
        'airport': airport
    }
    template = loader.get_template('airport/airport_detail.html')
    return HttpResponse(template.render(content, request))

def flights_view(request):
    flights = Flight.objects.all()
    content = {
        'flights': flights
    }
    template = loader.get_template('airport/flights.html')
    return HttpResponse(template.render(content, request))

def flight_detail_view(request, pk):
    flight = Flight.objects.get(pk=pk)
    content = {
        'flight': flight
    }
    template = loader.get_template('airport/flight_detail.html')
    return HttpResponse(template.render(content, request))
