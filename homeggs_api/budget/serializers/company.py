"""
Module of budget/serializers/company.py
"""

from . import serializers, UserSerializer, User, Company


class CreateCompanySerializer(serializers.Serializer):
    who = UserSerializer()
    name = serializers.CharField(max_length=20, allow_null=False)

    def create(self, validated_data):

        who = User.objects.get(id=validated_data['who'])

        if who:
            company = Company.objects.create(who=who.id, name=validated_data['name'])

            return company


class UpdateCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'