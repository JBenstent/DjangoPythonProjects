from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'employee' in request.session:
        return redirect('employees:emp_home')
    if 'appointment' in request.session:
        return redirect('appointments:app_home')
    return render(request, 'login/index.html')

def register_method(request):
    error = is_valid(request.POST['username'], request.POST['password'], request.POST['confirm'])
    if len(error) == 0:
        return redirect('employees:emp_home')
    else:
        return redirect('login:index')


def login_method(request):
    request.session['appointment'] = True
    request.session['username'] = request.POST['username']
    error = []

    check = True

    if len(request.POST['username']) == 0:
        check = False
        messages.add_message(request, messages.ERROR, 'username cannot be blank')

    if len(request.POST['password']) < 8:
        check = False
        messages.add_message(request, messages.ERROR, 'Password cannot be less than 8 characters long')

    if request.POST['password'] != request.POST['confirm']:
        messages.add_message(request, messages.ERROR, 'invalid password')
        check = False

    if check == True:
        return redirect('appointments:app_home')

def logout(request):
    request.session.clear()
    return redirect('login:index')

def is_valid(username, password, confirm):

    error = []

    if len(username) == 0:
        error.append('username cannot be blank')

    if len(password) < 8:
        error.append('password cannot be less than 8 characters')

    if password != confirm:
        error.append('invalid password')

    return error
