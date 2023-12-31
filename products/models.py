from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category_name


class Brand(models.Model):
    model_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.model_name


class Order(models.Model):
    product = models.ManyToManyField('Product')
    quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=200)
    stock_level = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
