"""
Module for Coast Serializer
"""

from . import serializers, Coast


class CoastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coast
        fields = '__all__'