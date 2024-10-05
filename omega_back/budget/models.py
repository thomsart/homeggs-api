from django.db import models

# Create your models here.
class Amount(models.Model):

    name = models.CharField(max_length=30, unique=True)
    active = models.BooleanField(default=True)
    price = models.IntegerField()
    cash = models.BooleanField(default=False)
    automatic_saved = models.BooleanField(default=False)
    created_date = models.DateField(auto_created=True)
    modified_date = models.DateField()
    start_month = models.DateField()
    each_year = models.SmallIntegerField(default=0)
    each_month = models.SmallIntegerField(default=0)
    due = price = models.SmallIntegerField(default=0)
    alert = models.BooleanField(default=False)