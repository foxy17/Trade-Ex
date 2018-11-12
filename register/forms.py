from django import forms
from django.contrib.auth import get_user_model
User=get_user_model()
class ContactForm(forms.Form):
	full_name=forms.CharField(
		widget=forms.TextInput(
			attrs={"class":"form-control",
			"placeholder":"Full Name",
			"id":"form_full_name"}))
	email=forms.EmailField(
		widget=forms.EmailInput(
			attrs={"class":"form-control",
			"placeholder":"E-mail",
			"id":"form_email"}))
	content=forms.CharField(
		widget=forms.Textarea(
			attrs={"class":"form-control",
			"placeholder":"Content",
			"id":"form_area"

			}
			)
			)

	def clean_email(self):
		email=self.cleaned_data.get("email")
		if not "@gmail.com" in email:
			raise forms.ValidationError("Email has to be gmail.com")

		return email

class LoginForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)
	def clean_username(self):
		username=self.cleaned_data.get('username')
		qs=User.objects.filter(username=username)
		if not qs.exists():
			print("Enter Valid Username")
			raise forms.ValidationError("Enter Valid Username")




class RegisterForm(forms.Form):
	username=forms.CharField()
	email=forms.EmailField(
		widget=forms.EmailInput(
			attrs={"class":"form-control",
			"placeholder":"E-mail",
			"id":"form_email"}))
	password=forms.CharField(widget=forms.PasswordInput)
	password2=forms.CharField(label='confirm password', widget=forms.PasswordInput)

	def clean_username(self):
		username=self.cleaned_data.get('username')
		qs=User.objects.filter(username=username)
		if qs.exists():
			print("Username is taken")
			raise forms.ValidationError("Username is taken")

		return username
	def clean_email(self):
		email=self.cleaned_data.get('email')
		qs=User.objects.filter(email=email)
		if qs.exists():
			print("email is taken")
			raise forms.ValidationError("E-mail is taken")

		return email
	def clean(self):
		data=self.cleaned_data
		password=self.cleaned_data.get('password')
		password2=self.cleaned_data.get('password2')
		arr=['@','$','#',"%","^","&","*","(",")"]

		if password2 !=password:
			print("Password must match")
			raise forms.ValidationError("Password must match")
		for i in arr:
			if i not in password:
				print("Password Must Contain any special character")
				raise forms.ValidationError("Password Must Contain any special character")
				break
		__all__="Password"
		return data
