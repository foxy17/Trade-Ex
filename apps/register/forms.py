from django import forms
from django.contrib.auth.models import User

from apps.register.models import UserProfile


class UserForm(forms.ModelForm):
    username=forms.CharField()
    class Meta:
        model = User
        fields = ["username", "email", "password"]




class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name','last_name')