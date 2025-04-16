"""
Module of shop/serializers/shop.py
"""

from . import serializers, Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'