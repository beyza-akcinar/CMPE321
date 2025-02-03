from django import forms

class manager_form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'password'}))