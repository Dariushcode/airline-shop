from django.contrib import admin
from .models import Airport, Flight

class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'departure_airport', 'arrival_airport', 'departure_time', 'arrival_time', 'price')
    search_fields = ('flight_number', 'departure_airport__name', 'arrival_airport__name')
    readonly_fields = ('last_update',)

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'location')
    search_fields = ('code', 'name')
    readonly_fields = ('last_update',)

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'departure_airport', 'arrival_airport', 'departure_time', 'arrival_time', 'price')
    search_fields = ('flight_number', 'departure_airport__name', 'arrival_airport__name')
    readonly_fields = ('last_update',)

admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
