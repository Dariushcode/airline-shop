from django.db import models
from city.models import Cities

class Airfare(models.Model):
    origin = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='origin_city')
    destination = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='destination_city')
    price = models.DecimalField(max_digits=999999999, decimal_places=0)
    date = models.DateField()

    def __str__(self):
        return f"{self.origin.title} to {self.destination.title}, Price: {self.price} , Date: {self.date}"