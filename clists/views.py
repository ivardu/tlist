from django.shortcuts import render, HttpResponseRedirect
# from django.conf.urls import HttpResponseRedirect

from clists.forms import CheckListForm, ItemsForm

# Create your views here.


def clist_landing_page(request):
	cform = CheckListForm()
	iform = ItemsForm()
	return render(request, 'clists/landing_page.htm', locals())