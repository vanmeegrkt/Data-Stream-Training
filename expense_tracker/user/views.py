from django.shortcuts import render,redirect
from .forms import UserForm,LoginForm
from .models import User_Data
from budget.models import Budget
from expenses.models import Expenses
from django.http import HttpResponse
from django.contrib import messages
import io
import base64
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import pandas as pd
from expenses.forms import ExpenseFilterForm
from django.db.models import Q

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            user = User_Data.objects.filter(username=username).first()
            Budget.objects.create(username=user, limit=0.00, current_amount=0.00)
            messages.info(request, "Account created Successfully!")
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User_Data.objects.filter(username=username, password=password).first()

            if user:
                request.session['username'] = username
                return redirect('home')
            else:
                form = LoginForm()
                error_msg = 'Invalid username or password!'
                return render(request, 'login.html', {'form': form, 'error_msg': error_msg})
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def home(request):

    username_str = request.session.get('username')
    if not username_str:
        messages.info(request, "Please login first!")
        return redirect('login')
    user_instance = User_Data.objects.get(username=username_str)
    expenses = Expenses.objects.filter(username=user_instance).values('category', 'amount')
    budget = Budget.objects.filter(username=user_instance).first()
    
    filter_form=ExpenseFilterForm(request.GET or None)
    expenses_query=Expenses.objects.filter(username=user_instance)
    if filter_form.is_valid():
        date=filter_form.cleaned_data.get('date')
        category=filter_form.cleaned_data.get('category')
        description=filter_form.cleaned_data.get('description')
        if category:
            expenses_query=expenses_query.filter(category=category)
        if date:
            expenses_query=expenses_query.filter(date__gte=date)
        if description:
            expenses_query=expenses_query.filter(description__icontains=description)
            
    expenses=expenses_query.values('category','amount')
    expenses_by_date=expenses_query.values('date','amount')
    
    if budget.current_amount<budget.limit:
        limit_message = "Current limit: Rs."+str(budget.limit)+" \nYou have exceeded the limit!"
    else:
        limit_message = f"Current limit: Rs.{budget.limit} \nYou have not exceeded the limit! You have Rs.{budget.current_amount-budget.limit} left!"

    if budget.current_amount<0:
        budget_message = f"You are in debt by Rs.{abs(budget.current_amount)}!"
    else:
        budget_message = f"You have Rs.{budget.current_amount} left!"

    active_filters={}
    if filter_form.is_valid():
        for field_name, field_value in filter_form.cleaned_data.items():
            if field_value:
                active_filters[field_name]=field_value

    if not expenses:
        return render(request, 'home.html', {
            'chart': None,
            'chart_1': None,
            'filter_form': filter_form,
            'active_filters': active_filters,
            'limit_message': limit_message,
            'budget_message': budget_message,
            'expenses_count': 0
        })
    
    df = pd.DataFrame(expenses)
    category_totals = df.groupby('category')['amount'].sum()

    plt.figure(figsize=(6, 6))
    plt.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%', startangle=140)
    plt.title('Expenses by Category')
    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode('utf-8')
    

    if not expenses_by_date:
        return render(request, 'home.html', {
            'chart': None,
            'chart_1': None,
            'filter_form': filter_form,
            'active_filters': active_filters,
            'limit_message': limit_message,
            'budget_message': budget_message,
            'expenses_count': 0
        })
    df=pd.DataFrame(expenses_by_date)
    df['date']=pd.to_datetime(df['date'])
    df['month']=df['date'].dt.to_period('M').astype(str)
    monthly_totals=df.groupby('month')['amount'].sum().reset_index()
    
    plt.figure(figsize=(10, 5))
    plt.bar(monthly_totals['month'], monthly_totals['amount'], color='skyblue')
    plt.xticks(rotation=45)
    plt.title('Monthly Expenses')
    plt.xlabel('Month')
    plt.ylabel('Total Amount')
    plt.tight_layout()
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic_1 = base64.b64encode(image_png).decode('utf-8')
    
    recent_expenses=expenses_query.order_by('-date')[:15]
    
    total_filtered_amount=sum(expense.amount for expense in expenses_query)
    return render(request, 'home.html', {
        'chart': graphic,
        'chart_1': graphic_1,
        'filter_form': filter_form,
        'active_filters': active_filters,
        'limit_message': limit_message,
        'budget_message': budget_message,
        'expenses_count': len(expenses_query),
        'recent_expenses': recent_expenses,
        'total_filtered_amount': total_filtered_amount
        
    })


def redirect_view(request):
    return redirect('user/login')

def logout(request):
    del request.session['username']
    return redirect('login')

