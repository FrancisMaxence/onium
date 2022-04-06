from django.db import models

class Supplier(models.Model):
    name = models.CharField(verbose_name='Supplier name', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
