"""
Module for Fee or Expense Model.
"""

from . import models


class FeeOrExpense(models.Model):
    """
    Expense like gas, food etc...
    """

    display_order = models.SmallIntegerField(default=0) # used when the user want to organize the display rank
    name = models.CharField(max_length=30, unique=True)
    active = models.BooleanField(default=True) # probably not applied every month cause of your situation
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0) # amount on month
    created_date = models.DateField(auto_now_add=True) # date set at creation only

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.name