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

    MONTHS = {
        "00": "",
        "01": "Janvier",
        "02": "Fevrier",
        "03": "Mars",
        "04": "Avril",
        "05": "Mai",
        "06": "Juin",
        "07": "Juillet",
        "08": "Aout",
        "09": "Septembre",
        "10": "Octobre",
        "11": "Novembre",
        "12": "Decembre"
    }

    display_order = models.SmallIntegerField(default=0, null=False) # used when the user want to organize the display rank
    tax = models.ForeignKey(Tax, default=None, on_delete=models.PROTECT)
    fee_or_expense = models.ForeignKey(FeeOrExpense, default=None, on_delete=models.PROTECT)
    name = models.CharField(max_length=30, unique=True, null=False)
    active = models.BooleanField(default=True, null=False) # you may want to stop to save cause of something
    automatically_deducted = models.BooleanField(default=True, null=False) # automated monthly bank fees
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=False) # the actual amount since you saved
    cash = models.BooleanField(default=False, null=False) # amount you want to take off from your bank account
    start_month = models.SmallIntegerField(choices=MONTHS, default=MONTHS["00"], null=False) # the month that you are supposed to pay or supposed to start to save
    year_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=False) # the total amount expected or due on a year
    due_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=False) # in considering the amount on a year and the actual amount 
    created_date = models.DateField(auto_now_add=True, null=False) # date set at creation only
    modified_date = models.DateField(auto_now=True, null=False) # date set at creation and on changed

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.name