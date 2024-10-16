from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

from .models import CustomUser, Status, Membership
from .forms import CustomUserCreationForm
from .managers import CustomUserManager



########### STATUS #######################################################

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name', 'level']


########### USER #########################################################

####################
class LoginCustomUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, clean_data):
        user = authenticate(email=clean_data['email'],
                            password=clean_data['password'])

        if not user:
            # raise ValidationError('user not found')
            return False
        return user
####################

class LightCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "phone"]

class HeavyCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "phone",
                  "days_off", "days_off_cumul", "permanent_contract"]

class CreateCustomUserSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=254)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    phone = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=128)

    def create(self, validated_data):

        status_name = validated_data.pop("status")
        status = Status.objects.get(name=status_name)
        user = CustomUser.objects.create_user(**validated_data)

        if user and status:
            user.hightest_level = status.level
            user.save()
            Membership.objects.create(user=user, status=status)

            return user


class UpdateCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "phone", "permanent_contract"]


########### MEMBERSHIP ###################################################

class LightMembershipSerializer(serializers.ModelSerializer):
    status = StatusSerializer()
    user = LightCustomUserSerializer()

    class Meta:
        model = Membership
        fields = ["id", "status", "user", "date"]

class HeavyMembershipSerializer(serializers.ModelSerializer):
    status = StatusSerializer()
    user = HeavyCustomUserSerializer()

    class Meta:
        model = Membership
        fields = ["id", "status", "user", "date"]

class CreateMembershipSerializer(serializers.Serializer):
    status = StatusSerializer()
    user = LightCustomUserSerializer()


    def to_internal_value(self, data):

        user = data.get('user')
        status = data.get('status')

        # Perform the data validation.
        if not user:
            raise serializers.ValidationError({
                'user': 'This field is required.'
            })
        if not status:
            raise serializers.ValidationError({
                'status': 'This field is required.'
            })

        # Return the validated values. This will be available as
        # the `.validated_data` property.
        return {
            'user': CustomUser.objects.get(id=user["id"]),
            'status': Status.objects.get(name=status["name"])
        }

    def create(self, validated_data):

        if Membership.objects.filter(**validated_data).exists():
            raise serializers.ValidationError({
                'status': 'The user is already a ' + validated_data['status'].name
            })

        membership = Membership.objects.create(**validated_data)
        membership.save()

        user = CustomUser.objects.get(pk=membership.user.pk)
        status = Status.objects.get(pk=membership.status.pk)

        if int(user.hightest_level) < int(status.level):
            user.hightest_level = status.level
            user.save()

        return membership
