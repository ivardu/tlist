from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
# from django.conf.urls import HttpResponseRedirect

from clists.forms import CheckListForm, ItemsForm
from clists.models import Items

# Create your views here.


def clist_landing_page(request):
	cform = CheckListForm()
	iform = ItemsForm()
	return render(request, 'clists/landing_page.htm', locals())


def create(request):

	return render(request, 'clists/create.html')


def items_form(request):
	if request.method == 'POST':
		iform = ItemsForm(request.POST)
		if iform.is_valid():
			iobj = iform.save()
			data = {
				'status': iobj.status,
				'items': iobj.items,
				'id':iobj.id,
			}
			return JsonResponse(data)

		else:
			print(iform.errors)



# Edit existing items model object


def items_data_edit(request, id):
	itm_obj = Items.objects.get(pk=id)
	print(itm_obj, request.POST['status'])
	if request.method == 'POST' and itm_obj:
		ieform = ItemsForm(request.POST, instance=itm_obj)
		if ieform.is_valid():
			obj = ieform.save()
			print(obj)
			data = { 
				'success':'success'
			}
			return JsonResponse(data)

		else:
			print(ieform.errors) 
