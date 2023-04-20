from rest_framework import serializers
from .models import CustomUser
from rest_framework import generics
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password','first_name','last_name','avatar')
        extra_kwargs = {
            'password': {'write_only': 'True'}
        }

    def validate_password(self, value): #Validation password
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user