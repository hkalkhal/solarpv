from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('welcome/', views.welcome, name='welcome'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # Clients urls
    path('dashboard/clients/', views.clients, name='clients'),
    path('dashboard/clients/create/', views.createClient, name='createClient'),
    path('dashboard/clients/delete/<int:id>/', views.deleteClient, name='deleteClient'),
    path('dashboard/clients/edit/<int:id>/', views.editClient, name='editClient'),
    # Certificates urls
    path('dashboard/certificates/', views.certificates, name='certificates'),
    path('dashboard/certificates/create/', views.createCertificate, name='createCertificate'),
    path('dashboard/certificates/delete/<int:id>/', views.deleteCertificate, name='deleteCertificate'),
    path('dashboard/certificates/edit/<int:id>/', views.editCertificate, name='editCertificate'),
    # Locations Urls
    path('dashboard/locations/', views.locations, name='locations'),
    path('dashboard/locations/create/', views.createLocation, name='createLocation'),
    path('dashboard/locations/delete/<int:id>/', views.deleteLocation, name='deleteLocation'),
    path('dashboard/locations/edit/<int:id>/', views.editLocation, name='editLocation'),
    # Products Urls
    path('dashboard/products/', views.products, name='products'),
    path('dashboard/products/create/', views.createProduct, name='createProduct'),
    path('dashboard/products/view//<int:id>/', views.viewProduct, name='viewProduct'),
    path('dashboard/products/delete/<int:id>/', views.deleteProduct, name='deleteProduct'),
    path('dashboard/products/edit/<int:id>/', views.editProduct, name='editProduct'),
    # Products Urls
    path('dashboard/standards/', views.standards, name='standards'),
    path('dashboard/standards/create/', views.createStandard, name='createStandard'),
    path('dashboard/standards/delete/<int:id>/', views.deleteStandard, name='deleteStandard'),
    path('dashboard/standards/edit/<int:id>/', views.editStandard, name='editStandard'),
    path('dashboard/standard/', views.standard, name='standard'),
    path('dashboard/certificate/', views.standard, name='standard'),
    path('test/', views.test, name='test'),
]