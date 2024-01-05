from django.contrib.auth.models import User
from django.db import models

from airlines.models import Airfare


class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class AirfareCountCart(models.Model):
    airfare=models.ForeignKey(Airfare,on_delete=models.CASCADE)
    count=models.PositiveIntegerField(default=1)
    cart = models.ForeignKey(ShoppingCart,on_delete=models.CASCADE)

