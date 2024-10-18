from django.db import models
# from django.contrib.auth.models import User
from account.models import User

# Create your models here.
class Salary(models.Model):
    """
    Salaries in the family.
    """

    who = models.ForeignKey(User, on_delete=models.PROTECT)
    company = models.CharField(max_length=15, null=False)
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=False) # amount of the salary
    created_date = models.DateField(auto_now_add=True, null=False) # date set at creation only


class Extra(models.Model):
    """
    Extra amounts for exemple sales or donations...
    """

    who = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=20, null=False)
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=False) # amount of the salary
    created_date = models.DateField(auto_now_add=True, null=False) # date set at creation only


class Tax(models.Model):
    """
    Tax represent here all kind of expenses you cannot avoid.
    """

    display_order = models.SmallIntegerField(default=0, null=False) # used when the user want to organize the display rank
    name = models.CharField(max_length=30, unique=True, null=False)
    active = models.BooleanField(default=True, null=False) # probably not applied every years cause of your situation
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=False) # amount on month
    automatically_deducted = models.BooleanField(default=True, null=False) # automated monthly bank fees
    created_date = models.DateField(auto_now_add=True, null=False) # date set at creation only

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.name


class FeeOrExpense(models.Model):
    """
    Expense like gas, food etc...
    """

    display_order = models.SmallIntegerField(default=0, null=False) # used when the user want to organize the display rank
    name = models.CharField(max_length=30, unique=True, null=False)
    active = models.BooleanField(default=True, null=False) # probably not applied every month cause of your situation
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=False) # amount on month
    created_date = models.DateField(auto_now_add=True, null=False) # date set at creation only

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.name


class ExceptionalExpense(models.Model):
    """
    Like it said by it's name, these are exceptionnals expenses...
    This allow to note in time life's problemes because sometimes we don't 
    realise why we have finacial troubles. Exemple: broken wash machine.
    """

    name = models.CharField(max_length=30, unique=True, null=False)
    note = models.TextField(max_length=100, default="")
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=False) # amount on month
    created_date = models.DateField(auto_now_add=True, null=False) # date set at creation only


class Saving(models.Model):
    """
    Saving represent here an amount for anything, it be can be also an amount 
    intended for a tax. This is why it possibly has a foreign key on Tax.
    """

    MONTHS = {
        "00": "",
        "01": "Janvier",
        "02": "Fevrier",
        "03": "Mars",
        "04": "Avril",
        "05": "Mai",
        "06": "Juin",
        "07": "Juillet",
        "08": "Aout",
        "09": "Septembre",
        "10": "Octobre",
        "11": "Novembre",
        "12": "Decembre"
    }

    display_order = models.SmallIntegerField(default=0, null=False) # used when the user want to organize the display rank
    tax = models.ForeignKey(Tax, default=None, on_delete=models.PROTECT)
    fee_or_expense = models.ForeignKey(FeeOrExpense, default=None, on_delete=models.PROTECT)
    name = models.CharField(max_length=30, unique=True, null=False)
    active = models.BooleanField(default=True, null=False) # you may want to stop to save cause of something
    automatically_deducted = models.BooleanField(default=True, null=False) # automated monthly bank fees
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=False) # the actual amount since you saved
    cash = models.BooleanField(default=False, null=False) # amount you want to take off from your bank account
    start_month = models.SmallIntegerField(choices=MONTHS, default=MONTHS["00"], null=False) # the month that you are supposed to pay or supposed to start to save
    year_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=False) # the total amount expected or due on a year
    due_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=False) # in considering the amount on a year and the actual amount 
    created_date = models.DateField(auto_now_add=True, null=False) # date set at creation only
    modified_date = models.DateField(auto_now=True, null=False) # date set at creation and on changed

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.name


###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################


class Product(models.Model):
    """
    This represent a product bought monthly. 
    """

    name = models.CharField(max_length=50, unique=True, null=False)
    quantity = models.SmallIntegerField(default=0)
    kilo = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    litre = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    supply = models.DateField(auto_now_add=True, null=False) # date set at creation only
    frequency = models.SmallIntegerField(default=0) # the frequency of consumption per date bought and quatity
    missing = models.BooleanField(default=False) # if the product is missing at home
    url = models.URLField(max_length=200, default="")
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default=None)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Shop(models.Model):
    """
    Shop where products are bought.
    """

    name = models.CharField(max_length=20, unique=True, null=False)
    km = models.DecimalField(max_digits=3, decimal_places=1, default=0) # distance from home
    url = models.URLField(max_length=200, default="")
    logo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default=None)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Coast(models.Model):
    """
    Many 2 many table in order to compare the cheapest products according to 
    shop prices.
    """

    product = models.ManyToManyField(Product)
    shop = models.ManyToManyField(Shop)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)