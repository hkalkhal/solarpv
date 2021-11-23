from django import forms
from .models import User, Client
from django.db.models import CharField


class SignForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(SignForm, self).__init__(*args, **kwargs)
        self.fields['userID'].widget.attrs = {'class': 'form-control',}
        self.fields['password'].widget.attrs = {'class': 'form-control',}
        self.fields['first_name'].widget.attrs = {'class': 'form-control',}
        self.fields['last_name'].widget.attrs = {'class': 'form-control',}
        self.fields['middle_name'].widget.attrs = {'class': 'form-control',}
        self.fields['job_title'].widget.attrs = {'class': 'form-control',}
        self.fields['email'].widget.attrs = {'class': 'form-control',}
        self.fields['office_phone'].widget.attrs = {'class': 'form-control',}
        self.fields['cell_phone'].widget.attrs = {'class': 'form-control',}
        self.fields['prefix'].widget.attrs = {'class': 'form-control',}
        self.fields['client_id'].widget.attrs = {'class': 'form-control',}


    class Meta:
        model = User
        fields = '__all__'



class SigninForm(forms.Form):
    username = forms.CharField(max_length=20, 
    widget=forms.TextInput(attrs= {'class' : 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=20,
    widget=forms.PasswordInput(attrs= {'class' : 'form-control', 'placeholder': 'Password'}))


# Client forms 

class ClientCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClientCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class': 'form-control',}
        self.fields['client_type'].widget.attrs = {'class': 'form-control',}

    class Meta:
        model = Client
        fields = '__all__'