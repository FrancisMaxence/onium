from django.contrib import admin

from products.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'upc',
        'supplier_code',
        'brand', 
        'description', 
        'weight', 
        'measure',
        'department'
        )
