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

from users.views import UserViewSet, GroupViewSet

from brands.views import BrandViewSet
from departments.views import DepartmentViewSet
from measures.views import MeasureViewSet
from suppliers.views import SupplierViewSet

router = routers.DefaultRouter()

# Users
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# Apps
router.register(r'brands', BrandViewSet, basename='brands')
router.register(r'departments', DepartmentViewSet, basename='departments')
router.register(r'measures', MeasureViewSet, basename='measures')
router.register(r'suppliers', SupplierViewSet, basename='suppliers')

# Url Patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
