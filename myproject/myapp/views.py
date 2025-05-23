from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import ContactForm

def home(request):
    return HttpResponse("Hello, Django!")

def hello(request):
    context = {'user_name': 'Vishwaa'}
    return render(request, 'home.html', context)    

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            return HttpResponse(f"Tank you, {name}! Your message: {message}")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})