from django.db import models

class Supplier(models.Model):
    name = models.CharField(verbose_name='Suppliers trademark', max_length=150)

    class Meta:
        ordering = ['name']
