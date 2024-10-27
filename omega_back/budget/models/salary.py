"""
Module for Salary Model.
"""

from . import models, User, Company


class Salary(models.Model):
    """
    Salaries in the family.
    """

    who = models.ForeignKey(User, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=False) # amount of the salary
    created_date = models.DateField(auto_now_add=True, null=False) # date set at creation only