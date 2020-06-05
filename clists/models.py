from django.db import models
from django.shortcuts import reverse
from users.models import TUser

# Create your models here.

STATUS_CHOICES = (
	('I','In Progress'),
	('C','Completed'),
	)


class CheckList(models.Model):
	title = models.CharField(max_length=255)
	date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(TUser, on_delete=models.CASCADE)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('clists:clistview',args=(self.id,))

	# def date_info(self):
	# 	return self.date.date()


class Items(models.Model):
	items = models.CharField(max_length=255)
	# status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	status = models.BooleanField(default=False)
	title = models.ForeignKey(CheckList, on_delete=models.CASCADE)

	class Meta:
		unique_together = ('items','title')


	def __str__(self):
		return f'{self.title}-{self.items}'


