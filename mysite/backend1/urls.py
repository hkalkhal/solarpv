from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('welcome/', views.welcome, name='welcome'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/clients/', views.clients, name='clients'),
    path('dashboard/clients/create/', views.client_create, name='client_create'),
    path('dashboard/clients/delete/<int:id>/', views.client_delete, name='client_delete'),
    path('dashboard/clients/edit/<int:id>/', views.client_edit, name='client_edit'),
    path('dashboard/location/', views.location, name='location'),
    path('dashboard/product/', views.product, name='product'),
    path('dashboard/standard/', views.standard, name='standard'),
    path('dashboard/certificate/', views.standard, name='standard'),
    path('test/', views.test, name='test'),
]