from django.forms import ModelForm
from .models import User_Data
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = User_Data
        fields = ['name', 'email', 'username', 'password', 'contact']

        widgets = {
           'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

