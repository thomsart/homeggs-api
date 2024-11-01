"""
Module for Tax Serializer
"""

from . import (
    serializers
)
from ..models import Tax

class CreateTaxSerializer(serializers.Serializer):
    display_order = serializers.IntegerField(default=0, allow_null=False)
    name = serializers.CharField(max_length=30, allow_null=False)
    active = serializers.BooleanField(default=True, allow_null=False)
    amount = serializers.DecimalField(max_digits=7, decimal_places=2, min_value=1.00, max_value=99999.99)
    automatically_deducted = serializers.BooleanField(default=True, allow_null=False)


class UpdateTaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = ["id", "display_order", "name", "active", "amount", "automatically_deducted"]


class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = '__all__'