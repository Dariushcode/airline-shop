from django.contrib import admin

from airlines.models import Airfare


class AirfareAdmin(admin.ModelAdmin):
    list_display = ('id', 'origin', 'destination', 'price', 'date')


admin.site.register(Airfare, AirfareAdmin)
