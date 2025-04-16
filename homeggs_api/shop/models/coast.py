"""
Module of shop/models/coast.py
"""

from . import models
from .product import Product
from .shop import Shop


class Coast(models.Model):
    """
    Many 2 many table in order to compare the cheapest products according to 
    shop prices.
    """

    product = models.ManyToManyField(Product)
    shop = models.ManyToManyField(Shop)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)