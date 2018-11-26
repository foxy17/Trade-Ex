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
from django.forms import modelformset_factory
from .forms import NoteForm,ImageForm
from .models import Notes,NoteImages



def post_create(request):

    ImageFormSet = modelformset_factory(NoteImages,
                                        form=ImageForm, extra=4,min_num=2)
    if request.method == 'POST':
        postForm = NoteForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=NoteImages.objects.none())
        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()
            for form in formset.cleaned_data:
                image = form['image']
                photo = NoteImages(note=post_form, image=image)
                photo.save()
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return redirect('index')
        else:
            print(NoteForm.errors, formset.errors)
    else:
        postForm = NoteForm()
        formset = ImageFormSet(queryset=NoteImages.objects.none())
    return render(request, 'Notes/post_form.html',
                  {'postForm': postForm, 'formset': formset}
                  )




def post_detail(request, slug=None):

    instance = get_object_or_404(Notes, slug=slug)

    ImageFormSet = modelformset_factory(ImageForm,
                                        form=ImageForm, extra=4)
    formset = ImageFormSet(queryset=NoteImages.objects.filter(note__exact=instance))



    if (formset != "" ): print("fuck yes")
    context = {
        "title": instance.topic,
        "instance": instance,


    }
    return render(request, "Notes/post_detail.html", context)


def post_list(request):
    today = timezone.now().date()
    queryset_list = Notes.objects.all()



    # queryset_list = Post.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(topic__icontains=query) |
            Q(subject__icontains=query)

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
    return render(request, "Notes/post_list.html", context)


def post_update(request, slug=None):
    instance = get_object_or_404(Notes, slug=slug)
    form = NoteForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.topic,
        "instance": instance,
        "form": form,
    }
    return render(request, "Post/post_form.html", context)


def post_delete(request, slug=None):
    instance = get_object_or_404(Notes, slug=slug)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("posts:list")