from clists.models import Items, CheckList, STATUS_CHOICES
from django import forms

class CheckListForm(forms.ModelForm):

	title = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control title_ip', 'placeholder':"What's the title.?"}))

	class Meta:
		model = CheckList
		fields = ['title']


class ItemsForm(forms.ModelForm):

	items = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control item-ip','placeholder':'Enter checklist items'}))
	# status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
	status = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'custom-control-input','id':'customSwitch1'}), required=False)
	class Meta:
		model = Items
		fields = ['items', 'status']