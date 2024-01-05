from django.urls import path

from airlines.views import airfare_view

urlpatterns = [
    path('airfares/', airfare_view),

]
