from django.urls import path
from clists import views as cvs 

urlpatterns = [
	path('create/', cvs.create, name='create'),
	path('items/', cvs.items_form, name='items_add'),
	path('items_edit/<int:id>/', cvs.items_data_edit, name='items_edit'),
]
