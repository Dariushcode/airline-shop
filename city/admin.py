from django.contrib import admin
from city.models import Ostan,Cities


class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('id','title','Ostan')

class CitiesAdmin(admin.ModelAdmin):
    list_display = ('id','title','city')

admin.site.register(Ostan)
admin.site.register(Cities)