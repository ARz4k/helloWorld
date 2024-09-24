from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def homeView(request):
    message='hello world !'

    return HttpResponse(message)

def aboutView(request):
    message='this is an about section of our project'

    return HttpResponse(message)

def contactView(request):
    return HttpResponse("This is a contact view")

def cartView(request):
    return HttpResponse("This is cart view")

class homeView(TemplateView):
    template_name = 'index.html'