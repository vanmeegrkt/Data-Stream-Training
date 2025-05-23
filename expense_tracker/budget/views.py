from django.shortcuts import render,redirect
from .forms import BudgetForm
from .models import Budget


def define_values(request):
    username = request.session.get('username')
    if not username:
        return redirect('login')
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            username = request.session.get('username')
            limit = form.cleaned_data['limit']
            current_amount = form.cleaned_data['current_amount']
            budget = Budget.objects.filter(username=username).first()
            budget.limit = limit
            budget.current_amount += current_amount
            budget.save()
            return redirect('home')
        else:
            return render(request, 'budget.html', {'form': form})
    else:
        username = request.session.get('username')
        budget = Budget.objects.filter(username=username).first()
        form = BudgetForm()
        return render(request, 'budget.html', {'form': form, 'budget': budget})
    