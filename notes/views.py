from main.settings import BASE_URL
from django.views.generic.edit import FormMixin, FormView

try:
    from urllib.parse import quote_plus
except:
    pass
from django.views.generic import DetailView, TemplateView, CreateView

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect,get_list_or_404
from django.utils import timezone
from django.forms import modelformset_factory, inlineformset_factory
from .forms import NoteForm
from .models import Notes



def post_create(request):
    postForm = NoteForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':


        if postForm.is_valid() :
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return redirect('notes:index1')
        else:
            print(NoteForm.errors)
    else:
        postForm = NoteForm()


    return render(request, 'Notes/post_form.html',
                  {'postForm': postForm,
                  }
                  )


# def post_create(request):
#
#
#     if request.method == 'POST':
#         postForm = NoteForm(request.POST)
#         form = ImageForm(request.POST, request.FILES)
#         if postForm.is_valid() and form.is_valid() :
#             post_form = postForm.save(commit=False)
#             post_form.user = request.user
#             post_form.save()
#             instance = NoteImages(file_field=request.FILES['file'],note=post_form)
#             instance.save()
#             files=request.FILES.getlist('file_field')
#             for f in files:
#                 NoteImages.objects.create(file=f, note=post_form)
#
#
#             messages.success(request,
#                              "Yeeew, check it out on the home page!")
#             return redirect('index')
#         else:
#             print(NoteForm.errors)
#     else:
#         postForm = NoteForm()
#         form = ImageForm()
#     return render(request, 'Notes/post_form.html',
#                   {'postForm': postForm,
#                    'fomr':form,}
#                   )




def post_detail(request, slug=None):

    instance = get_object_or_404(Notes, slug=slug)




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