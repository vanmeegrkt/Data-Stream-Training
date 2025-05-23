from django.urls import path
from . import views

urlpatterns = [
    path('expense/', views.view_expenses, name='view_expenses'),
    path('expenses/add/', views.add_expense, name='add_expense'),
    path('expenses/edit/<int:pk>/', views.edit_expense, name='edit_expense'),  #pk = primary key -> table : expenses id
]