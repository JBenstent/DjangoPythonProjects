from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *

def index(request):
    return render(request, 'login/index.html')

def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confirm = request.POST['confirm']

    errors = []
    errors += User.objects.validate_user(username, email, password, confirm)
    
    if len(errors) == 0:
        errors = User.objects.create_user(username, email, password)
        if len(errors) == 0:
            return redirect('login:success')
    
    for e in errors:
        messages.add_message(request, messages.ERROR, e)
        
    # experiment with reverse 'lookup'
    return redirect('login:index')

def success(request):
    return HttpResponse("SUCCESSFULLY CREATED USER")

def authenticate(request):
    username = request.POST['username']
    password = request.POST['password']
    if User.objects.authenticate_user(username, password):
        # give the proper redirect
        return redirect('login:success')
    else:
        messages.add_message(request, messages.ERROR, 'invalid login')
        return redirect('login:index')