from django.db import models


# Create your models here.

class Amount(models.Model):

    name = models.CharField(max_length=30, unique=True, null=False)
    active = models.BooleanField(default=True, null=False) # if you don't have this kind of fee at home
    compulsory_fees = models.BooleanField(default=False, null=False) # fee that you cannot avoid like governments' taxes
    display_order = models.SmallIntegerField(default=0) # used when the user want to organize the display rank
    automatically_deducted = models.BooleanField(default=False, null=False) # automated monthly bank fees
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=False) # the amount in euro or dollar
    cash = models.BooleanField(default=False, null=False) # amount you want to take off from your bank account

    created_date = models.DateField(auto_now_add=True, null=False) # date set at creation only
    modified_date = models.DateField(auto_now=True, null=False) # date set at creation and on changed

    start_month = models.SmallIntegerField(default=None) # the month that you are supposed to pay or supposed to start to save
    on_year = models.DecimalField(max_digits=7, decimal_places=2, default=None) # the total amount expected or due on a year
    late = models.DecimalField(max_digits=7, decimal_places=2, default=None) # in considering the amount on a year and the actual amount 

    # if compulsory_fee is not switch to True the last three fields will be considerate

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.__name__ + '.' + self.name


class Product(models.Model):

    name = models.CharField(max_length=50, unique=True, null=False)
    quantity = models.SmallIntegerField(default=None)
    kilo = models.DecimalField(max_digits=5, decimal_places=3, default=None)
    litre = models.DecimalField(max_digits=5, decimal_places=3, default=None)
    supply = models.DateField(auto_now_add=True, null=False) # date set at creation only
    frequency = models.SmallIntegerField(default=None) # the frequency of consumption per date bought and quatity
    missing = models.BooleanField(default=False) # if the product is missing at home
    url = models.URLField(max_length=200, default=None)
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default=None)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.__name__ + '.' + self.name


class Shop(models.Model):

    name = models.CharField(max_length=20, unique=True, null=False)
    km = models.DecimalField(max_digits=3, decimal_places=1, default=None) # distance from home
    url = models.URLField(max_length=200, default=None)
    logo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default=None)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.__name__ + '.' + self.name


class Price(models.Model):

    product = models.ManyToManyField(Product)
    shop = models.ManyToManyField(Shop)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=None)