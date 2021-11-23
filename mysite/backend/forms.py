from django import forms
from .models import User, Client, Certificate, Location, Product, TestStandard
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


# Certificates forms 
class CertificateCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CertificateCreateForm, self).__init__(*args, **kwargs)
        self.fields['UserID'].widget.attrs = {'class': 'form-control',}
        self.fields['report_type'].widget.attrs = {'class': 'form-control',}
        self.fields['issue_date'].widget.attrs = {'class': 'form-control',}
        self.fields['standard_ID'].widget.attrs = {'class': 'form-control',}
        self.fields['location_ID'].widget.attrs = {'class': 'form-control',}
        self.fields['model_number'].widget.attrs = {'class': 'form-control',}

    class Meta:
        model = Certificate
        fields = '__all__'

# Locations forms 
class LocationCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LocationCreateForm, self).__init__(*args, **kwargs)
        self.fields['address1'].widget.attrs = {'class': 'form-control',}
        self.fields['address2'].widget.attrs = {'class': 'form-control',}
        self.fields['city'].widget.attrs = {'class': 'form-control',}
        self.fields['state'].widget.attrs = {'class': 'form-control',}
        self.fields['postal_code'].widget.attrs = {'class': 'form-control',}
        self.fields['country'].widget.attrs = {'class': 'form-control',}
        self.fields['phone_number'].widget.attrs = {'class': 'form-control',}
        self.fields['fax_number'].widget.attrs = {'class': 'form-control',}
        self.fields['client_id'].widget.attrs = {'class': 'form-control',}


    class Meta:
        model = Location
        fields = '__all__'


# Products forms 
class ProductCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductCreateForm, self).__init__(*args, **kwargs)
        self.fields['model_number'].widget.attrs = {'class': 'form-control',}
        self.fields['product_name'].widget.attrs = {'class': 'form-control',}
        self.fields['cell_technology'].widget.attrs = {'class': 'form-control',}
        self.fields['cell_manufacturer'].widget.attrs = {'class': 'form-control',}
        self.fields['no_of_cells'].widget.attrs = {'class': 'form-control',}
        self.fields['no_of_cells_in_series'].widget.attrs = {'class': 'form-control',}
        self.fields['no_of_cells_in_strings'].widget.attrs = {'class': 'form-control',}
        self.fields['no_of_diodes'].widget.attrs = {'class': 'form-control',}
        self.fields['product_width'].widget.attrs = {'class': 'form-control',}
        self.fields['product_length'].widget.attrs = {'class': 'form-control',}
        self.fields['superstate_type'].widget.attrs = {'class': 'form-control',}
        self.fields['superstate_manufacturer'].widget.attrs = {'class': 'form-control',}
        self.fields['substrate_type'].widget.attrs = {'class': 'form-control',}
        self.fields['supstate_manufacturer'].widget.attrs = {'class': 'form-control',}
        self.fields['frame_type'].widget.attrs = {'class': 'form-control',}
        self.fields['frame_adhesive'].widget.attrs = {'class': 'form-control',}
        self.fields['encapsulate_type'].widget.attrs = {'class': 'form-control',}
        self.fields['encapsulate_manufacturer'].widget.attrs = {'class': 'form-control',}
        self.fields['junction_box_type'].widget.attrs = {'class': 'form-control',}
        self.fields['junction_box_manufacturer'].widget.attrs = {'class': 'form-control',}


    class Meta:
        model = Product
        fields = '__all__'


# Standards forms 
class StandardCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StandardCreateForm, self).__init__(*args, **kwargs)
        self.fields['standard_name'].widget.attrs = {'class': 'form-control',}
        self.fields['description'].widget.attrs = {'class': 'form-control',}
        self.fields['published_date'].widget.attrs = {'class': 'form-control',}

    class Meta:
        model = TestStandard
        fields = '__all__'

