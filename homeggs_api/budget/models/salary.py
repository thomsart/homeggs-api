"""
Module of budget/models/salary.py
"""

from . import models, User, Company


class Salary(models.Model):
    """
    Salaries in the family.
    """

    who = models.ForeignKey(User, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0.0) # amount of the salary
    created_date = models.DateField(auto_now_add=True) # date set at creation only