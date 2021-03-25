from django.shortcuts import render, redirect
from .models import usercreation
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# registration page
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = usercreation(request.POST)
            if form.is_valid():
                form.save()
                messages.info(request,'Account Created Successfully')
                return redirect('log_in')
        else:
            form = usercreation()
        return render(request,'register.html',{'form':form})

# login page
def log_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request,'Invalid Credentials, try again')
                return redirect('log_in')
        else:
            return render(request,'login.html')

#logout
def log_out(request):
    logout(request)
    messages.info(request,'Successfully logged out, Come back soon')
    return redirect('index')

