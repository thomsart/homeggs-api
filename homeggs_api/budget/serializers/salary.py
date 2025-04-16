"""
Module of budget/serializers/salary.py
"""

from . import (
    serializers, UserSerializer, CompanySerializer, User, Company, Salary
)

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


class UpdateSalarySerializer(serializers.ModelSerializer):
    class Salary:
        model = Salary
        fields = ["amount"]


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'