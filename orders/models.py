from django.contrib.auth.models import User
from django.db import models

from airlines.models import Airfare


class ShoppingOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)
    finalize = models.BooleanField(default=False)

    @property
    def total_price(self):
        sum_price = 0
        for airfares_count in self.order_airfare_count.all():
            sum_price += airfares_count.count * airfares_count.ticket.price
        return sum_price


class AirfareCountOrder(models.Model):
    airfare = models.ForeignKey(Airfare, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(ShoppingOrder, on_delete=models.CASCADE, related_name='order_airfare_count')
