from django import forms

class SignForm(forms.Form):
    username = forms.CharField(max_length=20, 
    widget=forms.TextInput(attrs= {'class' : 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=20,
    widget=forms.TextInput(attrs= {'class' : 'form-control', 'placeholder': 'Password'}))