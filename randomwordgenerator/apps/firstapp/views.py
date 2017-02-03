from django.shortcuts import render, redirect

def index(request):

    if 'counter' not in request.session:
        request.session['counter'] = 0

    return render(request, 'index.html')

def process(request):
    random_word = ""
    vowels = ['dasdf', 'a;lsdhjg', 'q8y245jxcv', 'aksjd yfwkzj', '9q3748tb']
    request.session['counter'] += 1
    request.session['word'] = random_word
    return redirect('/')

def clear(request):
    if 'counter' in request.session:
        request.session['counter'] = 0
    return redirect('/')
