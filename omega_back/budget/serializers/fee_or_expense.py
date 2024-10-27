"""
Module for Fee or Expense Serializer
"""

from . import serializers, FeeOrExpense


class FeeOrExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeOrExpense
        fields = '__all__'