"""
Module of budget/serializers/fee_or_expense.py
"""

from . import serializers, FeeOrExpense


class CreateFeeOrExpenseSerializer(serializers.Serializer):
    display_order = serializers.IntegerField(default=0, allow_null=False)
    name = serializers.CharField(max_length=30, allow_null=False)
    active = serializers.BooleanField(default=True, allow_null=False)
    amount = serializers.DecimalField(max_digits=7, decimal_places=2, min_value=1.00, max_value=99999.99)


class UpdateFeeOrExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeOrExpense
        fields = ["display_order", "name", "active", "amount"]


class FeeOrExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeOrExpense
        fields = '__all__'