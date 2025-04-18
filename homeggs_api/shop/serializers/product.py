"""
Module of shop/serializers/product.py
"""

from . import serializers, Product


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'kilo', 'litre']


class UpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name', 'quantity', 'kilo', 'litre', 'supply', 'frequency',
            'missing', 'url', 'photo'
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'