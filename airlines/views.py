from django.http import HttpResponse
from django.template import loader


from airlines.models import Airfare, Cities

def airfare_view(request):

    airfare = Airfare.objects.all()
    content = {
        'airfare': airfare
    }
    templates = loader.get_template('airfare/airfare.html')
    return HttpResponse(templates.render(content, request))
