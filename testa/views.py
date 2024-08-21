from django.shortcuts import render, redirect
from . models import List
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm
from django import forms 

def home(request):
    
    lists = List.objects.all()
    
    
    if request.method == "POST":
        username = request.POST['username']
        password= request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully Logged in")
            return redirect('home')
        
        else:
            messages.success(request, "You entered a wrong username, Try again!!!!")
            return redirect('home')
    
    else:
        return render(request, 'home.html', {'lists':lists})
        
    
    



def customer_record(request, pk):
    
    customer_record = List.objects.get(id=pk)
    return render(request, 'record.html', {'customer_record', customer_record})


def register_user(request):  
    
    
    form = UserRegisterForm()
    
    
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid:
            form.save()  
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered, Kindly Log in')
            return redirect('home')
        else:
            messages.success(request, 'There is an Error in your form, Try Again!!!!')
            return redirect('home')         
    
    else:
        return render(request, 'register.html', {'form':form})
           
    
    
        
    
    



def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect('home')