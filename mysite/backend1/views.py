from django.shortcuts import render
from .forms import SignForm, SigninForm, ClientCreateForm
from .models import Service, Product, Certificate, User, Client
from django.contrib import messages

# Create your views here.

def welcome(request):
    return render(request, 'solarpv/welcome.html')

def dashboard(request):
    return render(request, 'solarpv/dashboard.html')

def clients(request):
    c = Client.objects.all()
    context = {
        'clients': c,
    }
    return render(request, 'solarpv/clients/clients.html', context)

def client_create(request):
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

def client_edit(request, id):
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



def client_delete(request, id):
    client = Client.objects.get(id = id)
    client.delete()
    messages.success(request, ('Deletion successful'))
    return render(request, 'solarpv/clients/deleteclient.html')

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
                messages.success(request, ('Your signed in!'))
                return render(request, 'solarpv/dashboard.html')
            else:
                messages.error(request, ('Wrong Username and/or Password'))

        else:
            messages.error(request, ('Opps something went wrong'))

    else:
        form = SigninForm()
    
    return render(request, 'solarpv/signin.html', {'form': form})

