from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        "title": "Hello World !",
        "content": "This is home page"
    }
    if request.user.is_authenticated():
        context["premium_content"] = "Yeaaahhh"
    return render(request, "register/index.html", context)


# def about_page(request):
#     context = {
#         "title": "about page !",
#         "content": "This is about page"
#     }
#     return render(request, "carousel/bspart1.html", context)


# def contact_page(request):
#     contact_form = ContactForm(request.POST or None)
#     context = {
#         "title": "contact page !",
#         "content": "This is contact page",
#         "form": contact_form,
#         "brand": "Contact"
#     }
#     if contact_form.is_valid():
#         print(contact_form.cleaned_data)
#     # if request.method=="POST":
#     # 	print(request.POST)
#     # 	print(request.POST.get('full_name'))
#     # 	print(request.POST.get('email'))
#     # 	print(request.POST.get('content'))
#     return render(request, "contact/view.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in :")
    # print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        # print(request.user.is_authenticated())
        if user is not None:
            # print(request.user.is_authenticated())
            login(request, user)
            # return to success page
            # context['form']=LoginForm()
            return redirect("/login")
        else:
            # return an 'invalid login' error message
            print("Error")
    return render(request, "register/login.html", context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)