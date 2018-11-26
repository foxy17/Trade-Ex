from django import forms
from django.contrib.auth.models import User
from django.forms import Select

from apps.register.models import UserProfile, Review


class UserForm(forms.ModelForm):
    username=forms.CharField()
    class Meta:
        model = User
        fields = ["username", "email", "password"]




class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name','last_name')
class RatingForm(forms.ModelForm):

    class Meta:
        model = Review
        RATING_CHOICES = (
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
        )
        exclude=('user_name',)
        fields=('rating',)
        widgets = {
            "rating": Select(choices=RATING_CHOICES),
            "user_name":forms.HiddenInput(),
        }