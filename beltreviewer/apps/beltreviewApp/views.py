from django.shortcuts import render, redirect
import re
import bcrypt
from django.contrib import messages
from .models import User, Book, Review


def index(request):

    return render(request, 'beltreviewApp/index.html')

def register(request):

    if request.method == 'POST':
        check = True

        errors = []

        if len(request.POST['password']) < 8:
            messages.add_message(request, messages.ERROR, 'invalid password')
            check = False

        if request.POST['confirmpw'] != request.POST['password']:
            messages.add_message(request, messages.ERROR, 'Passwords do not match')
            check = False

        if len(request.POST['first_name']) == 0:
            messages.add_message(request, messages.ERROR, 'First name cannot be blank')
            check = False

        if len(request.POST['last_name']) == 0:
            messages.add_message(request, messages.ERROR, 'Last name cannot be blank')
            check = False
            # print errors

        if check ==  True:
            hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(password=hashed, first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])

        context = {
        'errors': errors
        }

    return redirect('/')

def login(request):
    error1 = []

    try:
        user = User.objects.get(email=request.POST['email'])
        if bcrypt.hashpw(request.POST['password'].encode(), user.password.encode()) == user.password:
            request.session['first_name'] = user.first_name
            request.session['id'] = user.id
            return redirect('/books')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid login')

    except:
        messages.add_message(request, messages.ERROR, 'Invalid login')

    context = {
    'error1': error1
    }

    return redirect('/')

def allbookspage(request):

    book = Book.objects.all()
    reviews = Review.objects.all()

    context = {
    'book': book,
    'reviews': reviews
    }

    return render(request, 'beltreviewApp/books.html', context)

def addbookspage(request):
    return render(request, 'beltreviewApp/add.html')

def submitbookinfo(request):
    if request.method == 'POST':
        if request.POST['author'] == "":
            author = request.POST['authors']
        else:
            author = request.POST['author']

        newbook = Book.objects.create(book_title=request.POST['book_title'], author=author)
        newbook.save()
        review = Review.objects.create(contents=request.POST['review'], rating=request.POST['rating'], book=newbook, user_id=request.session['id'])
        review.save()
        books = Book.objects.all()

        return redirect('/books/' + str(newbook.id))

def renderbookinfo(request, id):

    book = Book.objects.get(id=id)
    # review = Review.objects.get(id=book_id)

    context = {
    'book': book,
    # 'review': review
    }

    return render(request, 'beltreviewApp/booksinfo.html', context) #taking id from database

def addreview(request, id):
    review = Review.objects.create(contents=request.POST['review'], rating=request.POST['rating'], book_id=id, user_id=request.session['id'])
    review.save()
    return redirect('/books/' + str(id))

def renderuserinfo(request, id):
    user = User.objects.get(id=id)

    context = {
    'user': user
    }

    return render(request, 'beltreviewApp/userrender.html', context)
