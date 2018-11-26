from django import forms
from django.forms import RadioSelect, Select

from .models import Products


class PostForm(forms.ModelForm):

    class Meta:
        model =Products
        choices = (
            ('Electronics', 'Electronics'),
            ('Books', 'Books'),
            ('Services', 'Services'),
            ('Others', 'Others')
        )
        fields = [
            "title",
            "description",
            "media",
            "tag",
            "price"



    ]
        widgets = {
            "tag": Select(choices=choices),
        }

