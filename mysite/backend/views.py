from django.shortcuts import render
from rest_framework import viewsets
from .models import Service, Product, Certificate
from .serializers import ServiceSerializer, ProductSerializer, CertificateSerializer

# Create your views here.
class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CertificateView(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


