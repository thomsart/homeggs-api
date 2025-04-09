"""
Module for Shop Model.
"""

from . import models


class Shop(models.Model):
    """
    Shop where products are bought.
    """

    name = models.CharField(max_length=20, unique=True, null=False)
    km = models.DecimalField(max_digits=3, decimal_places=1, default=0.0) # distance from home
    url = models.URLField(max_length=200, default="")
    logo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default=None)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name