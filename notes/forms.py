from django import forms
from django.forms import RadioSelect, Select

from .models import Notes,NoteImages

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


        ]
        widgets = {
            "subject": Select(choices=choices),
        }


class ImageForm(forms.ModelForm):

    class Meta:
        model = NoteImages
        fields = ('image', )
    def geturl(self):
        return self.image
