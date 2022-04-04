from rest_framework import permissions, viewsets

from products.models import Product
from products.serializers import ProductSerializer

class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
