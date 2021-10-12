from django.http import HttpResponse
from django.shortcuts import render
from .forms import SignForm

# Create your views here.

def welcome(request):
    return render(request, 'solarpv/welcome.html')

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
    return render(request, 'solarpv/register.html')

def location(request):
    return render(request, 'solarpv/location.html')

def product(request):
    return render(request, 'solarpv/product.html')

def test(request):
    return render(request, 'solarpv/test.html')

def certificate(request):
    return render(request, 'solarpv/certificate.html')
