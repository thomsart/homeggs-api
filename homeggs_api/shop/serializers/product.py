"""
Module for Product Serializer
"""

from . import serializers, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'