from django.contrib import admin

from .models import (
    Coast, 
    Company, 
    ExceptionalExpense, 
    Extra, 
    FeeOrExpense, 
    Product, 
    Salary, 
    Saving, 
    Shop, 
    Tax
)

# Register your models here.
admin.site.register(Coast)
admin.site.register(Company)
admin.site.register(ExceptionalExpense)
admin.site.register(Extra)
admin.site.register(FeeOrExpense)
admin.site.register(Product)
admin.site.register(Salary)
admin.site.register(Saving)
admin.site.register(Shop)
admin.site.register(Tax)
