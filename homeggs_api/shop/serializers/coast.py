"""
Module of shop/serializers/coast.py
"""

from . import serializers, Coast


class CoastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coast
        fields = '__all__'