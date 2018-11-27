from django.contrib.auth.decorators import login_required

from apps.register.forms import UserForm, UserProfileForm
from django.http import  HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django.contrib import messages
from django.template import RequestContext

from .models import User


def index(request):
    return render(request, 'index.html')


def register(request):

    registered = False
    if request.method == 'POST':
        uform = UserForm(data=request.POST)
        pform = UserProfileForm(data=request.POST)
        if uform.is_valid() and pform.is_valid():

            user = uform.save()

            # form brings back a plain text string, not an encrypted password
            pw = user.password
            # thus we need to use set password to encrypt the password string
            user.set_password(pw)
            user.save()
            profile = pform.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            return redirect('/')
        else:
            print(uform.errors, pform.errors)
    else:
        uform = UserForm()
        pform = UserProfileForm()

    return render_to_response('accounts/signupnew.html', {'uform': uform, 'pform': pform, 'registered': registered}, RequestContext(request, {}))


# def register(request):
#     if request.method == 'POST':
#
#         errors = User.objects.validator(request.POST)
#         if len(errors):
#             for tag, error in errors.iteritems():
#                 messages.error(request, error, extra_tags=tag)
#             return redirect('/')
#
#         hashed_password = request.POST['password']
#         user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_password, email=request.POST['email'])
#
#         user.save()
#         request.session['id'] = user.id
#         authenticate(request, id=user.id)
#         return redirect('/success')
#     else:
#        return render(request,'accounts/signup.html')
#

# def log_in(request):
#     if request.method == 'POST':
#
#         if (User.objects.filter(email=request.POST['login_email']).exists()):
#             user = User.objects.filter(email=request.POST['login_email'])[0]
#             print(user.email)
#             if (request.POST['login_password']==user.password):
#                 request.session['id'] = user.id
#                 authenticate(request, email=user.email,password=user.password)
#
#                 return redirect('/success')
#         c = {
#             "error": 'Wrong email or password'
#         }
#         return render(request,'accounts/login.html',context=c)
#     else:
#         return render(request, 'accounts/login.html')





def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(username=username, password=password)
          if user is not None:
              if user.is_active:
                  login(request, user)

                  return render(request,'index.html')
              else:

                  return HttpResponse("You're account is disabled.")
          else:

              print ( "invalid login details " + username + " " + password)
              return render_to_response('accounts/newlogin.html', {}, context)
    else:

        return render_to_response('accounts/newlogin.html', {}, context)

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'register/success.html', context)

# def user_profile:


@login_required
def user_logout(request):
    context = RequestContext(request)
    logout(request)
    # Redirect back to index page.
    return HttpResponseRedirect('/')