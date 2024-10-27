"""
Module for Extra Serializer
"""

from . import serializers, Extra


class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model =Extra
        fields = '__all__'