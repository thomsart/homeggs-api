from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

from .models import User, Company, Salary, Extra, Tax, FeeOrExpense, ExceptionalExpense, Saving, Product, Shop, Coast
from account.serializers import UserSerializer


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CreateSalarySerializer(serializers.Serializer):
    who = UserSerializer()
    company = CompanySerializer()
    amount = serializers.DecimalField(max_digits=7, decimal_places=2, default=0)

    def create(self, validated_data):

        who = User.objects.get(id=validated_data['who'])
        company = Company.objects.get(id=validated_data['company'])

        if who and company:
            salary = Salary.objects.create(who=who.id, company=company.id, amount=validated_data['amount'])

            return salary


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'


class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model =Extra
        fields = '__all__'


class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = '__all__'


class FeeOrExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeOrExpense
        fields = '__all__'

class ExceptionalExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExceptionalExpense
        fields = '__all__'


class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class CoastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coast
        fields = '__all__'