"""
Module for Exceptional Expense Serializer
"""

from . import serializers, ExceptionalExpense


class ExceptionalExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExceptionalExpense
        fields = '__all__'