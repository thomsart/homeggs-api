from django.contrib import admin

from .models import (coast, 
                     company, 
                     exceptional_expense, 
                     extra, 
                     fee_or_expense, 
                     product, 
                     salary, 
                     saving, 
                     shop, 
                     tax )

# Register your models here.
admin.site.register(coast.Coast)
admin.site.register(company.Company)
admin.site.register(exceptional_expense.ExceptionalExpense)
admin.site.register(extra.Extra)
admin.site.register(fee_or_expense.FeeOrExpense)
admin.site.register(product.Product)
admin.site.register(salary.Salary)
admin.site.register(saving.Saving)
admin.site.register(shop.Shop)
admin.site.register(tax.Tax)
