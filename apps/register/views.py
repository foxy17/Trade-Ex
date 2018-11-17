

from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django.contrib import messages

from .models import User

def list(request):
    return render(request, 'register/list.html')
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':

        errors = User.objects.validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')

        hashed_password = request.POST['password']
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_password, email=request.POST['email'])

        user.save()
        request.session['id'] = user.id
        authenticate(request, id=user.id)
        return redirect('/success')
    else:
       return render(request,'accounts/signup.html')


def log_in(request):
    if request.method == 'POST':

        if (User.objects.filter(email=request.POST['login_email']).exists()):
            user = User.objects.filter(email=request.POST['login_email'])[0]
            print(user.email)
            if (request.POST['login_password']==user.password):
                request.session['id'] = user.id
                authenticate(request, email=user.email,password=user.password)

                return redirect('/success')
        c = {
            "error": 'Wrong email or password'
        }
        return render(request,'accounts/login.html',context=c)
    else:
        return render(request, 'accounts/login.html')

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'register/success.html', context)