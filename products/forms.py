from django import forms
from django.forms import RadioSelect, Select

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model =Post
        choices = (
            ('Electronics', 'Electronics'),
            ('Books', 'Books'),
            ('Services', 'Services'),
            ('Others', 'Others')
        )
        fields = (
            "title",
            "content",
            "image",
            "tag",
            "price"



    )
        widgets = {
            "tag": Select(choices=choices),
        }


