from django import forms

class director_form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'password'}))