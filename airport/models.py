from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True, blank=False, verbose_name='کد فرودگاه')
    name = models.CharField(max_length=255, blank=False, verbose_name='نام فرودگاه')
    location = models.CharField(max_length=255, blank=True, verbose_name='موقعیت مکانی')

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True, blank=False, verbose_name='شماره پرواز')
    departure_airport = models.ForeignKey(Airport, related_name='departures', blank=False, on_delete=models.CASCADE, verbose_name='فرودگاه حرکت')
    arrival_airport = models.ForeignKey(Airport, related_name='arrivals', blank=False, on_delete=models.CASCADE, verbose_name='فرودگاه ورود')
    departure_time = models.DateTimeField(blank=False, verbose_name='زمان حرکت')
    arrival_time = models.DateTimeField(blank=False, verbose_name='زمان ورود')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='قیمت بلیط')

    def __str__(self):
        return f"{self.flight_number} - {self.departure_airport.code} to {self.arrival_airport.code}"

    