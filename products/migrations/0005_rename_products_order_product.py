# Generated by Django 4.2.7 on 2023-11-12 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='products',
            new_name='product',
        ),
    ]