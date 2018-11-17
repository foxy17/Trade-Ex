from django.contrib.auth import authenticate
from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django.contrib import messages
from apps.register.models import User

from .models import products

def add_product(request):
    if request.method == 'POST':

        errors = products.objects.validator(request.POST)
        if len(errors):
            for tag1, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag1)
            return redirect('/')

        user = User.objects.get(id=request.session['id'])
        tags = request.POST['choice']
        product = products.objects.create(title=request.POST['title'], price=request.POST['price'], tags=tags, img=request.FILES['img'],description=request.POST['description'],)

        product.save()
        request.session['slug'] = product.slug

        return redirect('/success')
    else:
       return render(request,'accounts/signup.html')
