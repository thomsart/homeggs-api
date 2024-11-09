"""
Module for Exceptional Expense Serializer
"""

from . import serializers, ExceptionalExpense


class CreateExceptionalExpenseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    note = serializers.CharField(max_length=100, allow_null=True)
    amount = serializers.DecimalField(max_digits=7, decimal_places=2, min_value=1.00, max_value=99999.99)


class UpdateExceptionalExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExceptionalExpense
        fields = ['id', 'name', 'note', 'amount']


class ExceptionalExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExceptionalExpense
        fields = '__all__'