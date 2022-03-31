"""onium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from onium.users.views import UserViewSet, GroupViewSet
from onium.brands.views import BrandViewSet
from onium.measure.views import MeasureViewSet
from onium.suppliers.views import SupplierViewSet

router = routers.DefaultRouter()

# Users
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# Apps
router.register(r'brands', BrandViewSet)
router.register(r'measure', MeasureViewSet)
router.register(r'suppliers', SupplierViewSet)

# Url Patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
