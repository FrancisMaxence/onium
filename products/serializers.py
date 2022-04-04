from rest_framework import serializers

from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 
            'upc', 
            'supplier_code',
            'plu_code',
            'cash_register_code',
            'brand',
            'description',
            'weight',
            'case_size',
            'measure',
            'supplier',
            'department',
            'in_store'
            ]
