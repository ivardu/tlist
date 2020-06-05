from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView 
from django.urls import reverse_lazy
from .forms import SignUpForm

from .models import TUser


class SignUpView(CreateView):
	model = TUser
	form_class = SignUpForm
	template_name = 'users/signup.html'
	success_url = reverse_lazy('login')

	def form_valid(self, form):
		return super().form_valid(form)




