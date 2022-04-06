# Generated by Django 4.0.3 on 2022-04-06 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_brand'),
        ('brands', '0002_brand_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products_list', to='products.product'),
        ),
    ]
