from django import forms
from .models import Expenses

class ExpenseFilterForm(forms.Form):
    CATEGORY_CHOICES = [
        ('', 'All Categories'),
        ('Personal', 'Personal'),
        ('Friends', 'Friends'),
        ('Family', 'Family'),
    ]
    amount = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=False)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    description = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Search by description'})
    )


class ExpenseEditForm(forms.ModelForm):
    expense = forms.ModelChoiceField(
        queryset=Expenses.objects.none(),
        required=True,
        label="Select an Expense"
    )
    class Meta:
        model = Expenses
        fields = ['amount', 'category', 'date', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        username = kwargs.pop('username', None)
        super().__init__(*args, **kwargs)
        if username:
            self.fields['expense'].queryset = Expenses.objects.filter(username=username)

class ExpenseDeleteForm(forms.Form):
    expense = forms.ModelChoiceField(queryset=Expenses.objects.none(), required=True,label="Select an Expense")

    def __init__(self, *args, **kwargs):
        username = kwargs.pop('username', None)
        super().__init__(*args, **kwargs)
        if username:
            self.fields['expense'].queryset = Expenses.objects.filter(username=username)
        
        
    
