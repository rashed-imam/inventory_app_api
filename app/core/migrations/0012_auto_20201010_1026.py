# Generated by Django 2.2.16 on 2020-10-10 10:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_product_stock_alert_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customertrasnscation',
            name='order_time',
        ),
        migrations.RemoveField(
            model_name='vendortrasnscation',
            name='order_time',
        ),
        migrations.AddField(
            model_name='customer',
            name='created_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='modified_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='customerordereditems',
            name='created_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='customerordereditems',
            name='modified_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='customertrasnscation',
            name='created_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='customertrasnscation',
            name='modified_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='customertrasnscationbill',
            name='created_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='customertrasnscationbill',
            name='modified_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='moveproduct',
            name='created_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='moveproduct',
            name='modified_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='product',
            name='created_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='product',
            name='modified_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='shop',
            name='created_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='shop',
            name='modified_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='created_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='user',
            name='modified_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='vendor',
            name='created_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='vendor',
            name='modified_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='vendorordereditems',
            name='created_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='vendorordereditems',
            name='modified_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='vendortrasnscation',
            name='created_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='vendortrasnscation',
            name='modified_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='vendortrasnscationbill',
            name='created_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='vendortrasnscationbill',
            name='modified_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='created_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='modified_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='warehouseproducts',
            name='created_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='warehouseproducts',
            name='modified_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]