from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import TUser

# Register your models here.

class TUserAdmin(UserAdmin):
	form = UserChangeForm
	add_form = UserCreationForm
	list_display = ('email', 'signup_date')
	ordering = ('email',)
	fieldsets = (
			('UserInfo', {'fields':('email',)}),
		)
	# add_fieldsets = (('email',{'fields':'email'}),)


admin.site.register(TUser, TUserAdmin)
admin.site.unregister(Group)

