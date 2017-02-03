from django.shortcuts import render, redirect
from django.db import models
import random
import datetime


def index(request):


    if 'gold' not in request.session:
        request.session['gold'] = 0

    if 'log' not in request.session:
        request.session['log'] = []


    return render(request, 'index.html')

def process_money(request):

    now = datetime.datetime.now()
    if request.method == "POST":
        if request.POST['building'] == 'farm':
            number = random.randrange(0, 21)
            request.session['gold'] += number
            request.session['log'].append({'message': 'Earned ' + str(number) + ' golds ' + 'at the farm ' + str(now), 'color': 'red'})

        if request.POST['building'] == 'cave':
            number = random.randrange(5, 11)
            request.session['gold'] += number
            request.session['log'].append({'message': 'Earned ' + str(number) + ' golds ' + 'at the cave ' + str(now), 'color': 'blue'})

        if request.POST['building'] == 'house':
            number = random.randrange(2, 6)
            request.session['gold'] += number
            request.session['log'].append({'message': 'Earned ' + str(number) + ' golds ' + 'at the house ' + str(now), 'color': 'green'})

        if request.POST['building'] == 'casino':
            number = random.randrange(-51, 51)
            request.session['gold'] += number
            if number > 0:
                request.session['log'].append({'message': 'Earned ' + str(number) + ' golds ' + 'at the casino ' + str(now), 'color': 'black'})
            else:
                request.session['log'].append({'message': 'Lost ' + str(number) + ' golds ' + 'at the casino ' + str(now), 'color': 'black'})


    context = {
    'n': number
    }

    return render(request, 'index.html', context)

def reset(request):

    request.session.clear()


    return redirect('/')
