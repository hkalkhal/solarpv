from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('welcome/', views.welcome, name='welcome'),
    path('location/', views.location, name='location'),
    path('product/', views.product, name='product'),
    path('test/', views.test, name='test'),
    path('certificate/', views.certificate, name='certificate')
]