from django.http import HttpResponse

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