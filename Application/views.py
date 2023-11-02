from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.


def login(request):
    if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(request, username = username, password = password )
         if user is not None:
              login(request,user)
              return redirect('/dashboard')
         else:
             return render(request,'auth/login.html', messages.error(request,'Invalid username or password'),{'error': 'we do not have this details on our record, check and try again'})
    return render(request, 'auth/login.html')

def dashboard(request):
    return render(request,'dashboard.html')

def award(request):
        #award has three files how to use id to load  the files
        return render(request,'award/index.html' )


    
def bank(request):
    return render(request,'bank/index.html')

def bitcoin(request):
    return render(request,'bitcoin/index.html')


def dashboard(request):
    return render(request,'dashboard.html')


def dashboard(request):
    return render(request,'dashboard.html')
 



