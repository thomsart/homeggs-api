"""
Module for Shop Serializer
"""

from . import serializers, Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'