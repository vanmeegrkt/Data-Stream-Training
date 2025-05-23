from django.urls import path
from . import views

from user.views import logout

urlpatterns = [
    path('budget/', views.define_values, name='budget'),
    path('logout/',logout,name='logout'),
]