# Generated by Django 4.2.1 on 2023-06-06 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
