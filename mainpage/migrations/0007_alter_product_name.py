# Generated by Django 5.2.4 on 2025-07-12 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0006_product_sales_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='نام'),
        ),
    ]
