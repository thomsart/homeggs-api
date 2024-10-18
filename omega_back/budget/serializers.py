from rest_framework import serializers

from .models import Salary, Extra, Tax, FeeOrExpense, ExceptionalExpense, Saving, Product, Shop, Coast


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = []


class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model =Extra
        fields = [] 


class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = []


class FeeOrExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeOrExpense
        fields = []

class ExceptionalExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExceptionalExpense
        fields = []


class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = [] 


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = []


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = []


class CoastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coast
        fields = []