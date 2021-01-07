from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from Myway.models import ImPfle

class UsReg(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Your Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']
		widgets = {
		"first_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter First name"
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter last name"
			}),
		"username":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter your username",
			}),
		'email':forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter your email"
			})
		}

class Updf(ModelForm):
	class Meta:
		model = User
		fields =["username","email","first_name","last_name"]
		widgets ={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update Username",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Update Email id",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update Last Name",
			}),
		}