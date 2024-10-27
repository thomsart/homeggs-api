"""
Module for Tax Serializer
"""

from . import serializers, Tax


class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = '__all__'