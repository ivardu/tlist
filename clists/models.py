from django.db import models

# Create your models here.

STATUS_CHOICES = (
	('I','In Progress'),
	('C','Completed'),
	)


class Items(models.Model):
	items = models.CharField(max_length=255)
	# status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	status = models.BooleanField(default=False)


class CheckList(models.Model):
	title = models.CharField(max_length=255)
	date = models.DateTimeField(auto_now_add=True)
	items = models.ForeignKey(Items, on_delete=models.CASCADE)


