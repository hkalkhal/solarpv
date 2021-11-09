from django.urls import path, include
from . import views 
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('services', views.ServiceView)
router.register('products', views.ProductView)
router.register('certificates', views.CertificateView)


urlpatterns = [
    path('', include(router.urls))
]