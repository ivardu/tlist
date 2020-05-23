from clists.models import Items, CheckList, STATUS_CHOICES
from django import forms

class CheckListForm(forms.ModelForm):

	title = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control title_ip', 'placeholder':'Whats the title.?'}))

	class Meta:
		model = CheckList
		fields = ['title']


class ItemsForm(forms.ModelForm):

	items = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
	class Meta:
		model = Items
		fields = ['items', 'status']