from django.db import models
from .product_options import *


class Product(models.Model):
    product_image_blue = models.ImageField(upload_to='product_images')
    product_image_red = models.ImageField(upload_to='product_images')
    product_image_green = models.ImageField(upload_to='product_images')
    product_image_black = models.ImageField(upload_to='product_images')

    product_name = models.CharField(max_length=40)

    short_description = models.CharField(max_length=100)

    long_description = models.CharField(max_length=200)

    price = models.DecimalField(default=0.0, max_digits=999, decimal_places=2)

    # Stock
    red_small = models.IntegerField(default=0)
    red_medium = models.IntegerField(default=0)
    red_large = models.IntegerField(default=0)
    black_small = models.IntegerField(default=0)
    black_medium = models.IntegerField(default=0)
    black_large = models.IntegerField(default=0)
    green_small = models.IntegerField(default=0)
    green_medium = models.IntegerField(default=0)
    green_large = models.IntegerField(default=0)
    blue_small = models.IntegerField(default=0)
    blue_medium = models.IntegerField(default=0)
    blue_large = models.IntegerField(default=0)


class Invoice(models.Model):
    client_name = models.CharField(max_length=40)
    client_address = models.CharField(max_length=100)
    client_email = models.CharField(max_length=200)
    date = models.CharField(max_length=6)
    items = []
    total_price = models.CharField(max_length=6)
    delivery = models.CharField(max_length=6)
    grand_total = models.CharField(max_length=6)

