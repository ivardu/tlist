from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView
# from django.conf.urls import HttpResponseRedirect

from clists.forms import CheckListForm, ItemsForm
from clists.models import Items, CheckList


# Adding title for the CheckList Template
def add_title(request):
	if request.method == 'POST':
		tform = CheckListForm(request.POST)
		if tform.is_valid():
			tobj = tform.save()
			data = {
				'title':tobj.title,
				'id':tobj.id,
			}
			return JsonResponse(data)
		else:
			print(tform.errors)

# Ticklistt home page
def clist_landing_page(request):
	# cform = CheckListForm()
	# iform = ItemsForm()
	return render(request, 'clists/landing_page.htm')

# Checklist create view on the ticklistt web app
def create(request):
	cform = CheckListForm()
	iform = ItemsForm()
	return render(request, 'clists/create.html', locals())


def items_data_add(request, id):
	try:
		ctitle = CheckList.objects.get(pk=id)
		items = Items.objects.filter(title=ctitle, items__iexact=request.POST['items'])
		# print(not(items))
	except: 
		ctitle = None

	if request.method == 'POST' and ctitle and not(items):
		iform = ItemsForm(request.POST)
		if iform.is_valid():
			try:
				iobj = iform.save(commit=False)
				iobj.title = ctitle
				iobj.save()
				data = {
					'status': iobj.status,
					'items': iobj.items,
					'id':iobj.id,
				}

				return JsonResponse(data)

			# This will not run any more as we have added the items object in the if condition
			except IntegrityError as e:
				# print('running exception')
				# response = JsonResponse({'error':'Integrity Error DataExists'})
				# response.status_code = 409
				return JsonResponse({'status':'false','error':'Integrity Error DataExists'}, status=409)

	# 	Need to handle the form errors
	# 	else:
	# 		print(iform.errors)

	# Handling the no object (items) error
	else:
		# response = JsonResponse({'exists':'Entry Exists already'})
		# response.status_code = 500
		# print('issue..')
		# return JsonResponse(data)
		return JsonResponse({'exists':'Entry Exists already'}, status=409) 


# Edit existing items model object

def items_data_edit(request, id):
	try:
		itm_obj = Items.objects.get(pk=id)
	except:
		itm_obj = None

	if request.method == 'POST' and itm_obj:
		ieform = ItemsForm(request.POST, instance=itm_obj)
		if ieform.is_valid():
			obj = ieform.save()
			# print(obj)
			data = { 
				'success':'success'
			}
			return JsonResponse(data)

		# Handle the form errors
		else:
			print(ieform.errors)

	#Handle the No object error itm_obj
	else:
		pass 


def items_data_del(request, id):
	try:
		items = Items.objects.get(pk=id)
	except:
		items = None
	if request.method == 'DELETE' and items:
		items.delete()
		data = {
			'success':'removed'
		}
		return JsonResponse(data)



# Listview of the list of CheckList items created by user
class MyClists(ListView):
	model = CheckList
	template_name = 'clists/myclists.html'


# CheckList Template and it's Items DetailView
class ClistsView(DetailView):
	model = CheckList
	template_name = 'clists/clistsview.html'


# class ClistsDeleteView(DeleteView):
# 	model = CheckList
# 	success_url = reverse_lazy('myclists')


def clists_delete_view(request, id):
	try:
		# print('hello')
		cl = CheckList.objects.get(pk=id)
		# print(cl, 'hello')
	except:
		cl = None 

	if request.method == 'DELETE' and cl:
		cl.delete()
		data = {'count':CheckList.objects.count()}

		return JsonResponse(data)
