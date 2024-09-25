from django.urls import path
from pages.views import homeView
from pages.views import aboutView
from pages.views import cartView,contactView


urlpatterns = [
    path('', homeView),
    path('about/', aboutView, name='about'),
    path('contact/', contactView, name='contact'),
    path('cart/', cartView, name='cart')
]