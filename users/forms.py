from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import TUser

class SignUpForm(UserCreationForm):

	email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder':'Email'}))
	password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
	password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Re-Enter Password'}))
	class Meta:
		model = TUser
		# fields= ['email']
		fields = ['email','password1', 'password2']