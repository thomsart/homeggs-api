"""
Module for Extra Serializer
"""

from . import serializers, Extra, UserSerializer


class CreateExtraSerializer(serializers.Serializer):
    who = UserSerializer()
    name = serializers.CharField(max_length=20, allow_null=False)
    amount = serializers.DecimalField(max_digits=7, decimal_places=2, min_value=1.00, max_value=99999.99)


class UpdateExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra
        fields = ['id', 'name', 'amount']


class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model =Extra
        fields = '__all__'
