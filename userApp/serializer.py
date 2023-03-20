from rest_framework import serializers
from .models import CustomUser
from rest_framework import generics



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
   
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password','first_name','last_name')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user