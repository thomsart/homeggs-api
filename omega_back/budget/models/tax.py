"""
Module for Tax Model.
"""

from . import models


class Tax(models.Model):
    """
    Tax represent here all kind of expenses you cannot avoid.
    """

    display_order = models.SmallIntegerField(default=0) # used when the user want to organize the display rank
    name = models.CharField(max_length=30, unique=True)
    active = models.BooleanField(default=True) # probably not applied every years cause of your situation
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0) # amount on month
    automatically_deducted = models.BooleanField(default=True) # automated monthly bank fees
    created_date = models.DateField(auto_now_add=True) # date set at creation only

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.name