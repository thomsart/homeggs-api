"""
Module for Saving Serializer
"""

from . import serializers, Saving


class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = '__all__'