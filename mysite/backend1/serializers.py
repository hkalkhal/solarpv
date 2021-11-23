from rest_framework import serializers
from .models import Service, Product, Certificate

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['product_name', 'product_width', 'product_length', 'frame_type']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['service_name', 'description', 'is_fi_required', 'FI_required']

class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields = ['report_type', 'issue_date', 'model_number']