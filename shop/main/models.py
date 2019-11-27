from django.db import models
from .product_options import *

class Product(models.Model):
    product_image = models.ImageField(upload_to='main/static/shop/product_images/')

    product_name = models.CharField(max_length=40)

    short_description = models.CharField(max_length=100)

    long_description = models.CharField(max_length=200)

    price = models.CharField(max_length=6)

    stock = models.CharField(max_length=2)

    color = models.CharField(max_length=5, choices=colors())

    size = models.CharField(max_length=6, choices=size())

    quantity = models.CharField(max_length=2)