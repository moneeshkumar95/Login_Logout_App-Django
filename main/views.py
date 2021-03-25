from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request,'index.html')

# home page
def home(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        messages.info(request,'Please login to explore')
        return redirect('log_in')


