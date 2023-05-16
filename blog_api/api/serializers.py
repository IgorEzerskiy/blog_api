from rest_framework import serializers

from blog_api.models import Topic, Post, Comment


class TopicSerializer(serializers.ModelSerializer):
    prefers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Topic
        fields = ['title', 'description', 'prefers']


class PostSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    created_at = serializers.DateField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    contains = TopicSerializer(many=True)

    class Meta:
        model = Post
        fields = ['slug', 'title', 'text', 'created_at',
                  'updated_at', 'author', 'contains']

    #def create(self, validated_data):

