from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'main/index.html')


def login(request):
    return render(request, 'main/auth-form.html')


def registerPage(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'main/reg-form.html', context)


def registration(request):
    return render(request, 'main/reg-form.html')