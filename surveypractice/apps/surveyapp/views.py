from django.shortcuts import render

def index(request):
    request.session['counter'] = 0

    return render(request, 'index.html')

def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']

    if 'counter' in request.session:
        request.session['counter'] += 1

    return render(request, 'results.html')
