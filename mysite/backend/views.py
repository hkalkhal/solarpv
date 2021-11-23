from django.shortcuts import render
from .forms import SignForm, SigninForm, ClientCreateForm, CertificateCreateForm, LocationCreateForm, ProductCreateForm, StandardCreateForm
from .models import Service, Product, Certificate, User, Client, Location, TestStandard
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.

def welcome(request):
    return render(request, 'solarpv/welcome.html')

def dashboard(request):
    return render(request, 'solarpv/dashboard.html')


# Dashboard Clients 
def clients(request):
    c = Client.objects.all()
    context = {
        'clients': c,
    }
    return render(request, 'solarpv/clients/clients.html', context)

def createClient(request):
    if request.method == 'POST':
        form = ClientCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your client was successfully added!'))
            return render(request, 'solarpv/clients/clients.html')

        else:
            messages.error(request, ('Your entry was not recorded'))

    else:
        form = ClientCreateForm()
    
    return render(request, 'solarpv/clients/createclient.html', {'form': form})

def editClient(request, id):
    obj= Client.objects.get(id=id)
    form = ClientCreateForm(request.POST or None, instance= obj)
    if form.is_valid():
        obj= form.save(commit= False)
        obj.save()
        context= {'form': form}
        messages.success(request, ('Your client was successfully edited!'))
        return render(request, 'solarpv/clients/editclient.html', context)

    else:
        context= {'form': form,'error': 'The form was not updated successfully. Please enter in a name and type'}
        return render(request,'solarpv/clients/editclient.html' , context)

def deleteClient(request, id):
    client = Client.objects.get(id = id)
    client.delete()
    messages.success(request, ('Deletion successful'))
    return render(request, 'solarpv/clients/deleteclient.html')

# Dashboard Certificates
def certificates(request):
    c = Certificate.objects.all()
    context = {
        'certificates': c,
    }
    return render(request, 'solarpv/certificates/certificates.html', context)

def createCertificate(request):
    if request.method == 'POST':
        form = CertificateCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your Certificate was successfully added!'))
            return render(request, 'solarpv/certificates/certificates.html')

        else:
            messages.error(request, ('Your entry was not recorded'))

    else:
        form = CertificateCreateForm()
    
    return render(request, 'solarpv/certificates/createcertificate.html', {'form': form})

def editCertificate(request, id):
    obj= Certificate.objects.get(id=id)
    form = CertificateCreateForm(request.POST or None, instance= obj)
    if form.is_valid():
        obj= form.save(commit= False)
        obj.save()
        context= {'form': form}
        messages.success(request, ('Your certificate was successfully edited!'))
        return render(request, 'solarpv/certificates/editcertificate.html', context)

    else:
        context= {'form': form,'error': 'The form was not updated successfully. Please enter in a name and type'}
        return render(request,'solarpv/certificates/editcertificate.html' , context)

def deleteCertificate(request, id):
    certificate = Certificate.objects.get(id = id)
    certificate.delete()
    messages.success(request, ('Deletion successful'))
    return render(request, 'solarpv/certificates/deletecertificate.html')


# Dashboard Locations
def locations(request):
    c = Location.objects.all()
    context = {
        'locations': c,
    }
    return render(request, 'solarpv/locations/locations.html', context)

def createLocation(request):
    if request.method == 'POST':
        form = LocationCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your location was successfully added!'))
            return render(request, 'solarpv/locations/locations.html')

        else:
            messages.error(request, ('Your entry was not recorded'))

    else:
        form = LocationCreateForm()
    
    return render(request, 'solarpv/locations/createlocation.html', {'form': form})

def editLocation(request, id):
    obj= Location.objects.get(id=id)
    form = LocationCreateForm(request.POST or None, instance= obj)
    if form.is_valid():
        obj= form.save(commit= False)
        obj.save()
        context= {'form': form}
        messages.success(request, ('Your location was successfully edited!'))
        return render(request, 'solarpv/locations/editlocation.html', context)

    else:
        context= {'form': form,'error': 'The form was not updated successfully. Please check errors'}
        return render(request,'solarpv/locations/editlocation.html' , context)

def deleteLocation(request, id):
    location = Location.objects.get(id = id)
    location.delete()
    messages.success(request, ('Deletion successful'))
    return render(request, 'solarpv/locations/deletelocation.html')


# Dashboard Products
def products(request):
    c = Product.objects.all()
    context = {
        'products': c,
    }
    return render(request, 'solarpv/products/products.html', context)

def viewProduct(request, id):
    obj= Product.objects.get(id=id)
    context = {
        'product': obj,
    }
    return render(request, 'solarpv/products/viewproduct.html', context)


def createProduct(request):
    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your product was successfully added!'))
            return render(request, 'solarpv/products/products.html')

        else:
            messages.error(request, ('Your entry was not recorded'))

    else:
        form = ProductCreateForm()
    
    return render(request, 'solarpv/products/createproduct.html', {'form': form})

def editProduct(request, id):
    obj= Product.objects.get(id=id)
    form = ProductCreateForm(request.POST or None, instance= obj)
    if form.is_valid():
        obj= form.save(commit= False)
        obj.save()
        context= {'form': form}
        messages.success(request, ('Your product was successfully edited!'))
        return render(request, 'solarpv/products/editproduct.html', context)

    else:
        context= {'form': form,'error': 'The form was not updated successfully. Please check error list'}
        return render(request,'solarpv/products/editproduct.html' , context)

def deleteProduct(request, id):
    product = Product.objects.get(id = id)
    product.delete()
    messages.success(request, ('Deletion successful'))
    return render(request, 'solarpv/products/deleteproduct.html')


# Dashboard Standards
def standards(request):
    c = TestStandard.objects.all()
    context = {
        'standards': c,
    }
    return render(request, 'solarpv/standards/standards.html', context)

def createStandard(request):
    if request.method == 'POST':
        form = StandardCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your standard was successfully added!'))
            return render(request, 'solarpv/standards/standards.html')

        else:
            messages.error(request, ('Your entry was not recorded'))

    else:
        form = StandardCreateForm()
    
    return render(request, 'solarpv/standards/createstandard.html', {'form': form})

def editStandard(request, id):
    obj= TestStandard.objects.get(id=id)
    form = StandardCreateForm(request.POST or None, instance= obj)
    if form.is_valid():
        obj= form.save(commit= False)
        obj.save()
        context= {'form': form}
        messages.success(request, ('Your standard was successfully edited!'))
        return render(request, 'solarpv/standards/editstandard.html', context)

    else:
        context= {'form': form,'error': 'The form was not updated successfully. Please enter in a name and type'}
        return render(request,'solarpv/standards/editstandard.html' , context)

def deleteStandard(request, id):
    standard = TestStandard.objects.get(id = id)
    standard.delete()
    messages.success(request, ('Deletion successful'))
    return render(request, 'solarpv/standards/deletestandard.html')



def location(request):
    return render(request, 'solarpv/location.html')

def product(request):
    return render(request, 'solarpv/product.html')

def certificate(request):
    return render(request, 'solarpv/certificate.html')

def standard(request):
    return render(request, 'solarpv/standard.html')

def test(request):
    certs = Certificate.objects.all()
    context = {
        'certs': certs,
    }
    return render(request, 'solarpv/test.html', context)

def certificate(request):
    return render(request, 'solarpv/certificate.html')

def index(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            return render(request, 'solarpv/welcome.html')
    else:
        form = SignForm()
    
    context = {'form' : form}
    return render(request, 'solarpv/index.html', context)

def register(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your user was successfully added!'))
            signform = SignForm()
            return render(request, 'solarpv/signin.html', {'form': signform})

        else:
            messages.error(request, ('Your entry was not recorded'))

    else:
        form = SignForm()
    
    return render(request, 'solarpv/register.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            passw = form.cleaned_data.get('password')
            if (User.objects.filter(userID=username).filter(password=passw).exists()):
                user = User.objects.get(userID=username)
                if(user.client_id.client_type == "Staff"):
                    messages.success(request, ('You signed in!'))
                    return redirect('dashboard')
                    # return render(request, 'solarpv/dashboard.html')
                else:
                    messages.success(request, ('You signed in!'))
                    return redirect('test')
                    # return render(request, 'solarpv/test.html')
            else:
                messages.error(request, ('Wrong Username and/or Password'))
                form = SigninForm()
                return render(request, 'solarpv/signin.html')

        else:
            messages.error(request, ('Opps something went wrong'))
            return render(request, 'solarpv/signin.html')

    else:
        form = SigninForm()
        return render(request, 'solarpv/signin.html', {'form': form})

