"""
Module for Company Model.
"""

from . import models, User


class Company(models.Model):
    """
    Company where come from salaries.
    """

    who = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=20, null=False)
    created_date = models.DateField(auto_now_add=True, null=False) # date set at creation only