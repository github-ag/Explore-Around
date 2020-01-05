from django import forms

class NameForm(forms.Form):
	placeName = forms.CharField(label='', max_length=100)

class MailForm(forms.Form):
	name = forms.CharField(label='', max_length=100)
	mail = forms.CharField(label='', max_length=100)
	subject = forms.CharField(label='', max_length=100)
	query = forms.CharField(label='', max_length=100)

class TwoForm(forms.Form):
	fromName = forms.CharField(label='', max_length=100)
	toName = forms.CharField(label='', max_length=100)
