from django.contrib import admin

from .models import (
    Coast, 
    Product, 
    Shop
)

# Register your models here.
admin.site.register(Coast)
admin.site.register(Product)
admin.site.register(Shop)