from django.shortcuts import render, redirect, HttpResponse

def employees(request):

    if 'username' not in request.session:
        return redirect('login:index')
    else:
        return HttpResponse('This is the employees app')
