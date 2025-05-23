from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from expenses.models import Expenses
from .serializers import ExpensesSerializer

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Add an expense': 'create-expense/',
        'Update an expense': 'update-expense/',
        'Get an expense': 'get-expense/',
        'Delete an expense': 'delete-expense/',
    }
    return Response(api_urls)

@api_view(['GET'])
def view_expenses(request):
    expenses = Expenses.objects.all()
    serializer = ExpensesSerializer(expenses, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_expense(request):
    serializer = ExpensesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def edit_expense(request, pk):
    try:
        expense = Expenses.objects.get(pk=pk)
    except Expenses.DoesNotExist:
        return Response({'error': 'Expense not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ExpensesSerializer(expense, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
