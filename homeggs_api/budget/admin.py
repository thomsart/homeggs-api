"""
Module of budget/admin.py
"""

from django.contrib import admin

from .models import (
    Company, 
    ExceptionalExpense, 
    Extra, 
    FeeOrExpense, 
    Salary, 
    Saving, 
    Tax
)

# Register your models here.
admin.site.register(Company)
admin.site.register(ExceptionalExpense)
admin.site.register(Extra)
admin.site.register(FeeOrExpense)
admin.site.register(Salary)
admin.site.register(Saving)
admin.site.register(Tax)
