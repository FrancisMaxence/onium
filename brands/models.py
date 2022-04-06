from django.db import models

class Brand(models.Model):
    name = models.CharField(verbose_name='Brand name', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
