from django.contrib import admin
from django.urls import path
from pages.views import homeView
from pages.views import aboutView
from pages.views import cartView,contactView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homeView),
    path('about/', aboutView),
    path('contact/', contactView),
    path('cart/', cartView)
]
