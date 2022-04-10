from django.db import models

from brands.models import Brand
from departments.models import Department
from measures.models import Measure
from suppliers.models import Supplier

class Product(models.Model):
    upc = models.IntegerField(unique=True)
    supplier_code = models.CharField(max_length=20, null=True, blank=True)
    plu_code = models.IntegerField(null=True, blank=True) # Make it unique or delete it ?
    cash_register_code = models.IntegerField(null=True, blank=True) # Make it unique or delete it ?
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True) # Make it mandatory !
    description = models.CharField(max_length=150)
    weight = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True) # Make it mandatory !
    measure = models.ForeignKey(Measure, on_delete=models.PROTECT, null=True, blank=True) # Make it mandatory !
    case_size = models.IntegerField(blank=True, default=1, null=True) # Make it mandatory !
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, null=True, blank=True) # Make it mandatory !
    department = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, blank=True) # Make it mandatory !
    in_store = models.BooleanField(null=True, blank=True) # Make it mandatory !

    class Meta:
        ordering = ['brand', 'description']