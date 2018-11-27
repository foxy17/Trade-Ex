from django.contrib.auth.decorators import login_required

from apps.register.forms import RatingForm, UserForm
from apps.register.models import Review
from main.settings import BASE_URL

try:
    from urllib.parse import quote_plus
except:
    pass
from django.views.generic import DetailView

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm
from .models import Products



def post_create(request):

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user

        print(instance.user.email)
        instance.save()
        # message success
        print('saved')
        messages.success(request, "Successfully Created")
        return redirect('index')
    context = {
        "form": form,
    }
    return render(request, "Post/post.html", context)


# class PostDetailView(DetailView):
#     template_name = 'Post/post_detail.html'
#
#     def get_object(self, *args, **kwargs):
#         slug = self.kwargs.get("slug")
#         instance = get_object_or_404(Products, slug=slug)
#         return instance
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(PostDetailView, self).get_context_data(**kwargs)
#         instance = context['object']
#         context['share_string'] = quote_plus(instance.content)
#         return context
#



def post_detail(request, slug=None):
    instance = get_object_or_404(Products, slug=slug)
    instance2=Review.objects.filter(user_name=instance.user.get_username())

    l = 0
    sum, i = 0, 0
    for r in instance2:
        l += (r.rating)
        print(l)
        i = i + 1
    if (i == 0):
        avg = "no rating"
    else:
        avg = l / i

    if(Review.objects.filter(user_name=instance.user.get_username())!=None ):
        context = {
            "title": instance.title,
            "instance": instance,
            "avg": avg,

        }
        return render(request, "Post/post_detail.html", context)

    else:
        rating=RatingForm(request.POST or None)
        rating.user_name=instance.user.get_username()
        if rating.is_valid():
            rate=rating.save(commit=False)
            rate.user_name=instance.user.get_username()
            print(rate.user_name)
            rate.save()
        context = {
            "title": instance.title,
            "instance": instance,
            "form":rating,
            "avg":avg,

        }
        return render(request, "Post/post_detail.html", context)


def post_list(request):
    today = timezone.now().date()
    queryset_list = Products.objects.all()

    # queryset_list = Post.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)


        ).distinct()
    paginator = Paginator(queryset_list, 8)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var,
        "today": today,
    }
    return render(request, "Post/post_list.html", context)


def post_update(request, slug=None):
    instance = get_object_or_404(Products, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "Post/post_form.html", context)


def post_delete(request, slug=None):
    instance = get_object_or_404(Products, slug=slug)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("index")