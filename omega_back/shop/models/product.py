"""
Module for Product Model.
"""

from . import models


class Product(models.Model):
    """
    This represent a product bought monthly. 
    """

    name = models.CharField(max_length=50, unique=True, null=False)
    quantity = models.SmallIntegerField(default=0)
    kilo = models.DecimalField(max_digits=5, decimal_places=3, default=0.0)
    litre = models.DecimalField(max_digits=5, decimal_places=3, default=0.0)
    supply = models.DateField(auto_now_add=True, null=False) # date set at creation only
    frequency = models.SmallIntegerField(default=0) # the frequency of consumption per date bought and quatity
    missing = models.BooleanField(default=False) # if the product is missing at home
    url = models.URLField(max_length=200, default="")
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default=None)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name