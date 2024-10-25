from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

from .models import User
from .forms import UserCreationForm
from .managers import UserManager


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, clean_data):
        user = authenticate(email=clean_data['email'],
                            password=clean_data['password'])

        if not user:
            # raise ValidationError('user not found')
            return False
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "phone"]


class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=254)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    phone = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=128)

    def create(self, validated_data):

        user = User.objects.create_user(**validated_data)

        if user:
            user.save()

            return user


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "phone"]
