from django.urls import path

from airport.views import airport_detail_view, airports_view, books_view, book_detail_view, category_view, flight_detail_view, flights_view, publisher_view


urlpatterns = [
    path('airports/', airports_view, name='airports'),
    path('airports/<int:pk>/', airport_detail_view, name='airport_detail'),
    path('flights/', flights_view, name='flights'),
    path('flights/<int:pk>/', flight_detail_view, name='flight_detail'),
]
