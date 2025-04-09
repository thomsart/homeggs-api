"""
Module for Exceptional Expense Model.
"""

from . import models


class ExceptionalExpense(models.Model):
    """
    Like it said by it's name, these are exceptionnals expenses...
    This allow to note in time life's problemes because sometimes we don't 
    realise why we have finacial troubles. Exemple: broken wash machine.
    This allows also to note expenses like presents or holydays etc...
    """

    name = models.CharField(max_length=30, unique=True)
    note = models.TextField(max_length=100, null=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0.0) # amount on month
    created_date = models.DateField(auto_now_add=True) # date set at creation only