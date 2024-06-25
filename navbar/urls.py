from django.urls import path

from .views import home,contact,department,about,doctors,booking

urlpatterns = [
    path('',home,name='home'),
    path('contact',contact,name='contact'),
    path('department',department,name='department'),
    path('about',about,name='about'),
    path('doctors',doctors,name='doctors'),
    path('booking',booking,name='booking'),
]