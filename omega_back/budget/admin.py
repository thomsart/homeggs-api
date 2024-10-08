from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.Amount)
admin.site.register(models.Product)
admin.site.register(models.Shop)
admin.site.register(models.Price)
