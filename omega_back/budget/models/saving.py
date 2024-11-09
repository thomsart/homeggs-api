"""
Module for Saving Model.
"""

from . import models
from .tax import Tax
from .fee_or_expense import FeeOrExpense


class Saving(models.Model):
    """
    Saving represent here an amount for anything, it be can be also an amount 
    intended for a tax. This is why it possibly has a foreign key on Tax.
    """

    class Month(models.IntegerChoices):
        NULL: 0
        JANUARY: 1
        FEBRUARY: 2
        MARCH: 3
        APRIL: 4
        MAY: 5
        JUNE: 6
        JULLY: 7
        AUGUST: 8
        SEPTEMBER: 9
        OCTOBER: 10
        NOVEMBER: 11
        DECEMBER: 12

    display_order = models.SmallIntegerField(default=0) # used when the user want to organize the display rank
    tax = models.ForeignKey(Tax, null=True, on_delete=models.PROTECT)
    fee_or_expense = models.ForeignKey(FeeOrExpense, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=30, unique=True)
    active = models.BooleanField(default=True) # you may want to stop to save cause of something
    automatically_deducted = models.BooleanField(default=True) # automated monthly bank fees
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.0) # the actual amount since you saved
    cash = models.BooleanField(default=False) # amount you want to take off from your bank account
    start_month = models.IntegerField(choices=Month, default=0) # the month that you are supposed to pay or supposed to start to save
    year_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0.0) # the total amount expected or due on a year
    due_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0.0) # in considering the amount on a year and the actual amount 
    created_date = models.DateField(auto_now_add=True) # date set at creation only
    modified_date = models.DateField(auto_now=True) # date set at creation and on changed

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.name