"""
Module of budget/serializers/saving.py
"""

from . import (
    serializers, Saving, FeeOrExpenseSerializer
)
from .tax import TaxSerializer

class CreateSavingSerializer(serializers.Serializer):
    display_order = serializers.IntegerField(default=0, allow_null=False)
    tax = TaxSerializer(allow_null=True)
    fee_or_expense = FeeOrExpenseSerializer(allow_null=True)
    name = serializers.CharField(max_length=30, allow_null=False)
    active = serializers.BooleanField(default=True, allow_null=False)
    automatically_deducted = serializers.BooleanField(default=True, allow_null=False)
    amount = serializers.DecimalField(max_digits=8, decimal_places=2, min_value=1.00, max_value=999999.99)
    cash = serializers.BooleanField(default=False, allow_null=False)
    start_month = serializers.ChoiceField(choices=Saving.Month, allow_null=False)
    year_amount = serializers.DecimalField(max_digits=7, decimal_places=2, min_value=1.00, max_value=99999.99)
    due_amount = serializers.DecimalField(max_digits=7, decimal_places=2, min_value=1.00, max_value=99999.99)


class UpdateSavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = [
            "display_order", "active", "automatically_deducted", 
            "amount", "cash", "start_month", "year_amount", "due_amount"
        ]

class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = '__all__'