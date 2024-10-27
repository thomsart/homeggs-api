"""
Module for Tax Model.
"""

from . import models


class Tax(models.Model):
    """
    Tax represent here all kind of expenses you cannot avoid.
    """

    display_order = models.SmallIntegerField(default=0, null=False) # used when the user want to organize the display rank
    name = models.CharField(max_length=30, unique=True, null=False)
    active = models.BooleanField(default=True, null=False) # probably not applied every years cause of your situation
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=False) # amount on month
    automatically_deducted = models.BooleanField(default=True, null=False) # automated monthly bank fees
    created_date = models.DateField(auto_now_add=True, null=False) # date set at creation only

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.name