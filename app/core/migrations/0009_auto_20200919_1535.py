# Generated by Django 2.2.16 on 2020-09-19 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_customerordereditems_product_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='customertrasnscationbill',
            name='due',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vendorordereditems',
            name='product_detail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendor_product_detail', to='core.Product'),
        ),
    ]