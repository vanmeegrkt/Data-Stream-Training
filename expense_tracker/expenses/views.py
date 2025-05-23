from django.shortcuts import render, redirect
from .forms import ExpenseFilterForm
from .models import Expenses
from budget.models import Budget
from user.models import User_Data
from .forms import ExpenseEditForm, ExpenseDeleteForm

def create_expense(request):
    username = request.session.get('username')
    if not username:
        return redirect('login')
    if request.method == 'POST':
        form = ExpenseFilterForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            category = form.cleaned_data['category']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']
            username = request.session.get('username')
            user = User_Data.objects.get(username=username) 
            expense = Expenses.objects.create(
                amount=amount,
                category=category,
                date=date,
                description=description,
                username=user
            )
            expense.save()
            budget = Budget.objects.filter(username=username).first()
            budget.current_amount -= amount
            budget.save()
            return redirect('home')
        else:
            return render(request, 'create_expense.html', {'form': form})
    else:
        form = ExpenseFilterForm()
        return render(request, 'create_expense.html', {'form': form})
    
def edit_expense_view(request):
    username = request.session.get('username')
    if not username:
        return redirect('login')
    selected_expense = None

    if request.method == 'POST':
        form = ExpenseEditForm(request.POST, username=username)
        if form.is_valid():
            selected_expense = form.cleaned_data['expense']
            old_expense_amount = selected_expense.amount
            selected_expense.amount = form.cleaned_data['amount']
            selected_expense.category = form.cleaned_data['category']
            selected_expense.date = form.cleaned_data['date']
            selected_expense.description = form.cleaned_data['description']
            selected_expense.save()
            budget = Budget.objects.filter(username=username).first()
            if old_expense_amount > selected_expense.amount:
                budget.current_amount += old_expense_amount - selected_expense.amount
            else:
                budget.current_amount -= selected_expense.amount - old_expense_amount
            budget.save()

            return redirect('home') 
    else:
        form = ExpenseEditForm(username=username)

    return render(request, 'edit_expense.html', {'form': form})

def delete_expense(request):
    username = request.session.get('username')
    if not username:
        return redirect('login')
    if request.method == 'POST':
        form = ExpenseDeleteForm(request.POST, username=username)
        if form.is_valid():
            selected_expense = form.cleaned_data['expense']
            budget = Budget.objects.filter(username=username).first()
            budget.current_amount += selected_expense.amount
            budget.save()
            selected_expense.delete()
            return redirect('home')
    else:
        form = ExpenseDeleteForm(username=username)
    return render(request, 'delete_expense.html', {'form': form})