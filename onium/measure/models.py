from django.db import models

class Measure(models.Model):
    name = models.CharField(max_length=4)

    class Meta:
        ordering = ['name']
