from django.urls import path
from . import views

urlpatterns = [
    path('expense/', views.create_expense, name='expense'),
    path('edit/', views.edit_expense_view, name='edit_expense'),
    path('delete/', views.delete_expense, name='delete_expense'),
]