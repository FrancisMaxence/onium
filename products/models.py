from django.db import models

from brands.models import Brand
from departments.models import Department
from measures.models import Measure
from suppliers.models import Supplier

class Product(models.Model):
    upc = models.IntegerField(unique=True)
    supplier_code = models.CharField(max_length=20, null=True, blank=True)
    plu_code = models.IntegerField(unique=True, null=True, blank=True)
    cash_register_code = models.IntegerField(unique=True, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    weight = models.DecimalField(max_digits=8, decimal_places=2)
    measure = models.ForeignKey(Measure, on_delete=models.PROTECT)
    case_size = models.IntegerField(blank=True, default=1)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    in_store = models.BooleanField()

    class Meta:
        ordering = ['brand', 'description']