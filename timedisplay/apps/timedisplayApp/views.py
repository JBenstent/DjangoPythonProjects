from django.shortcuts import render
import datetime


def index(request):

    now = datetime.datetime.now()

    context = {
    'currenttime' : now
    }


    return render(request, 'index.html', context)
