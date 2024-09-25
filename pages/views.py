from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.

def homeView(request):
    return render(request,'home.html')

def aboutView(request):
    return render(request,'about.html')

def contactView(request):
    return render(request,'contact.html')

def cartView(request):
    return render(request,'cart.html')

# class homeView(TemplateView):
#     template_name = 'index.html'

# class aboutView(TemplateView):
#     template_name = 'about.html'

# class contactView(TemplateView):
#     template_name = 'contact.html'

# class cartView(TemplateView):
#     template_name = 'cart.html'