from django.shortcuts import render, HttpResponse

def index(request):

    return HttpResponse('No Ninjas Here!')

def allninjas(request):

    return render(request, 'index.html')


def show(request, color):

    if color == 'orange':
        michaelangelo = 'http://vignette3.wikia.nocookie.net/vsbattles/images/a/ac/Mikey.png/revision/latest?cb=20150805115441'
        context = {
        'color' : michaelangelo
        }
    elif color == 'red':
        raphael = 'https://sites.google.com/a/clipartonline.net/teenage-mutant-ninja-turtles/_/rsrc/1392049222538/raphael-ninja-turtle/raphael-tmnt_3.png?height=400&width=400'
        context = {
        'color': raphael
        }

    elif color == 'blue':
        donatello = 'https://upload.wikimedia.org/wikipedia/pt/archive/2/2f/20151216161043!Donatello-2003-cartoon.jpg.jpg'
        context = {
        'color': donatello
        }

    else:
        megan = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_zIUxHlR85luPjECd0PTyM45y5aVT8ZyB5XhmmdXeJWXNmswb'
        context = {
        'color': megan
        }
    return render(request, 'show.html', context)
