from django.db import models

class Department(models.Model):
    name = models.CharField(verbose_name='Department name', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
