# Generated by Django 2.2.16 on 2020-09-15 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200915_0817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendortrasnscation',
            name='delivery_warehouse',
        ),
        migrations.AddField(
            model_name='vendorordereditems',
            name='delivery_warehouse',
            field=models.ForeignKey(null=True, on_delete=None, to='core.Warehouse'),
        ),
    ]
