from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, "main/dashboard.html")

def login(request):
    context = {}
    return render(request, "main/login.html", context)

def register(request):
    form = UserCreationForm
    context = {'form':form}
    return render(request, "main/register.html", context)