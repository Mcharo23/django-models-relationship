# Generated by Django 4.2.7 on 2023-11-12 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=500),
            preserve_default=False,
        ),
    ]