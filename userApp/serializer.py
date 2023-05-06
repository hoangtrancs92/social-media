from rest_framework import serializers
from .models import CustomUser
from rest_framework import generics
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(required=False)
    def get_avatar(self, obj):
        avatar_url = obj.avatar.url
        api_media_prefix = 'media/'
        print(avatar_url)
        return api_media_prefix + avatar_url + '/'
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password','first_name','last_name','avatar']
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
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        password = validated_data.get('password')
        if password:
            instance.set_password(password)

        avatar = validated_data.get('avatar')
        if avatar:
            instance.avatar.save(avatar.name, avatar)

        instance.save()

        return instance
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        password = validated_data.get('password')
        if password:
            instance.set_password(password)

        avatar = validated_data.get('avatar')
        if avatar:
            instance.avatar.save(avatar.name, avatar)

        instance.save()

        return instance

class UserRetrieveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email','first_name','last_name','avatar']
    def get_avatar(self, obj):
        avatar_url = obj.avatar.url
        api_media_prefix = 'media/'
        print(avatar_url)
        return api_media_prefix + avatar_url + '/'