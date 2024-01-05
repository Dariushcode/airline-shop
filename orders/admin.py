from django.contrib import admin

from orders.models import ShoppingOrder, AirfareCountOrder


@admin.register(ShoppingOrder)
class ShoppingOrderAdmin(admin.ModelAdmin):
    pass

@admin.register(AirfareCountOrder)
class AirfareCountOrderAdmin(admin.ModelAdmin):
    pass
