from django import forms
from django.forms import RadioSelect, Select

from .models import Notes

class NoteForm(forms.ModelForm):

    class Meta:
        model = Notes
        choices = (
            ('Subject1', 'Subject1'),
            ('Subject2', 'Subject2'),
            ('Subject3', 'Subject3'),
            ('Subject4', 'Subject4')
        )
        fields = [
            "subject",
            "topic",
            "notes",
            "image",
            "image1",
            "image2",
            "image3",


        ]
        widgets = {
            "subject": Select(choices=choices),
        }

