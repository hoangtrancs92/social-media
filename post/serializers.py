from rest_framework.serializers import ModelSerializer
from .models import *

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']