from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from carts.models import ShoppingCart, AirfareCountCart
from airlines.models import Airfare


@login_required
def shopping_cart_view(request):
    user_shopping_cart = ShoppingCart.objects.get(user=request.user)

    airfare_in_cart = AirfareCountCart.objects.filter(cart=user_shopping_cart)

    context = {
        'airfare_in_cart': airfare_in_cart
    }
    return render(request, 'cart/shopping_cart.html', context)


def add_to_cart(request):
    if request.method == 'POST':
        air_id = request.POST.get('air_id')
        airfare = get_object_or_404(Airfare, pk=air_id)

        shopping_cart, created = ShoppingCart.objects.get_or_create(user=request.user)
        airfare_count_cart, created = AirfareCountCart.objects.get_or_create(cart=shopping_cart, airfare=airfare)
        if not created:
            airfare_count_cart.count = airfare_count_cart.count + 1
        airfare_count_cart.save()

        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def remove_book(request):
    if request.method == 'POST':
        airfare_id = request.POST.get('airfare_id')
        airfare = get_object_or_404(Airfare, pk=airfare_id)
        shopping_cart = get_object_or_404(ShoppingCart, user=request.user)
        airfare_count_cart = get_object_or_404(AirfareCountCart, cart=shopping_cart, book=airfare)
        if airfare_count_cart.count < 2:
            airfare_count_cart.delete()
        else:
            airfare_count_cart.count = airfare_count_cart.count - 1
            airfare_count_cart.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
