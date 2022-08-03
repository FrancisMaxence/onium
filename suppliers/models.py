from django.db import models

class Supplier(models.Model):
    RETURN_CHOICES = [
        ('C', 'Crédits'),
        ('P', 'Pertes')
    ]

    name = models.CharField(verbose_name='Supplier name', max_length=150)
    return_policy = models.CharField(verbose_name=' Return policy', choices=RETURN_CHOICES, max_length=500, default='P')
    comments = models.CharField(verbose_name='Comments', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
