from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.



class TUser(AbstractUser):
	username = None
	signup_date = models.DateTimeField(auto_now_add=True)

	email = models.EmailField(unique=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()


	def __str__(self):
		return self.email
