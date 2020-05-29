from django.urls import path
from clists import views as cvs 

urlpatterns = [
	path('create/', cvs.create, name='create'),
	path('items/<int:id>/', cvs.items_data_add, name='items_add'),
	path('items_edit/<int:id>/', cvs.items_data_edit, name='items_edit'),
	path('items_del/<int:id>/', cvs.items_data_del, name='items_del'),
	path('title/',cvs.add_title, name='add_title'),
	path('myclists/', cvs.MyClists.as_view(), name='myclists'),
	path('clistview/<int:pk>/',cvs.ClistsView.as_view(), name='clistview'),
	path('clist_delete/<int:id>/', cvs.clists_delete_view, name='clist_del'),
]
