from django import forms

class BudgetForm(forms.Form):
    limit = forms.DecimalField(max_digits=10, decimal_places=2,initial=0.00,label="Set Limit")
    current_amount = forms.DecimalField(max_digits=10, decimal_places=2,initial=0.00,label="Add Budget")
