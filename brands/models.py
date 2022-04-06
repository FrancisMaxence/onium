from django.db import models

class Brand(models.Model):
    name = models.CharField(verbose_name='Brand name', max_length=150)
    products = models.ForeignKey('products.Product', on_delete=models.PROTECT, related_name='products_list', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
