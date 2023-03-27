from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','link','user']

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')

    def get_image(self, course):
        if course.image:
            request = self.context.get('request')
            return request.build_absolute_uri('/static/%s' % course.image.name) if request else ''
class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']
class PostDetailSerializer(PostSerializer):
    tags = TagSerializer(many=True)
    class Meta: 
        model = PostSerializer.Meta.model
        fields = PostSerializer.Meta.fields + ['description', 'tags']

class DiscussionSerializer(serializers.ModelSerializer):
    # Khai báo khóa ngoại
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), source='post', write_only=True)
    class Meta:
        model = Discussion
        fields = ['id', 'parent_id', 'type', 'content','post_id']
    def validate_content(self, value):
        if value is None:
            raise serializers.ValidationError("Content cannot be null!")
        return value

class AuctionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        models = AuctionHistory
        fields = '__all__'