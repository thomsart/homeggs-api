"""
Module for Extra Model.
"""

from . import models, User


class Extra(models.Model):
    """
    Extra amounts for exemple sales or donations...
    """

    who = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0.0) # amount of the salary
    created_date = models.DateField(auto_now_add=True) # date set at creation only