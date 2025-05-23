from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello', views.hello, name='hello'),
    path('contact', views.contact, name='contact'),
]