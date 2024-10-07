from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.Amount, models.Product, models.Shop, models.Price)