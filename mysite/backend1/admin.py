from django.contrib import admin
from .models import Client, User, Location, TestStandard, Service, Product, Certificate, PerformanceData

# Register your models here.
admin.site.register(Client)
admin.site.register(User)
admin.site.register(Location)
admin.site.register(TestStandard)
admin.site.register(Service)
admin.site.register(Product)
admin.site.register(Certificate)
admin.site.register(PerformanceData)
