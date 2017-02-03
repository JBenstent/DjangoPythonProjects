from django.shortcuts import render, redirect
from .models import Email
import re


def index(request):

    return render(request, 'emailApp/index.html')

def isvalid(request):

    if request.method == "POST":

        email_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        result = email_re.match(request.POST['emailaddress'])


        emails = Email.objects.all()

        error = []
        context = {
        'error': error,
        'emails': emails
        }
        if not result:
            error.append('Email is not valid')

            return render(request, 'emailApp/index.html', context)
        else:
            Email.objects.create(emails=request.POST['emailaddress'])
            error.append('Congratulations')
            return render(request, 'emailApp/success.html', context)

def success(request):

    return render(request, 'emailApp/success.html')

def delete(request):

    allemails = Email.objects.all()
    allemails.delete()


    return redirect('emailApp/success.html')
