from django.db import models

class Measure(models.Model):
    name = models.CharField(max_length=4)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
