from django import forms
from viewapp.models import client

class loginfrom(forms.Form):
    email = forms.CharField(label='email', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class createForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    priority = forms.IntegerField()
    created_by  = forms.CharField()
    #  class Meta:
    #     model = client
    #     fields = "__all__"

class updateForm(forms.Form):
    id=forms.IntegerField()
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    priority = forms.IntegerField()
    created_by  = forms.CharField()