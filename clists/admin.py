from django.contrib import admin
from .models import CheckList, Items

# Register your models here.

@admin.register(CheckList)
class CheckListAdmin(admin.ModelAdmin):
	list_display = ('title','date')
	ordering = ('date',)
	search_fields = ('title','date')


class ItemsAdmin(admin.ModelAdmin):
	list_display = ('items','title', 'status')
	ordering = ('status',)
	search_fields = ('items','title','status')

admin.site.register(Items, ItemsAdmin)