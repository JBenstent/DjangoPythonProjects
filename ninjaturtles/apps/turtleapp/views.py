from django.shortcuts import render

def index(request):

    return render(request, 'turtleapp/index.html')

def allfour(request):

    return render(request, 'turtleapp/allfour.html')

def process(request, color):

    context = {
    'color' : color
    }

    return render(request, 'turtleapp/multipleoutputs.html', context)
