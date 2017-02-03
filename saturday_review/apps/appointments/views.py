from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'username' in request.session:
        return render(request, 'login/appt.html')
    else:
        return redirect('login:index')
