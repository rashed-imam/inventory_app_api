# Generated by Django 2.2.16 on 2020-09-11 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_customertrasnscationbill'),
    ]

    operations = [
        migrations.AddField(
            model_name='customertrasnscationbill',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Shop'),
        ),
    ]
