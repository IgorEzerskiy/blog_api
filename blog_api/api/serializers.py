from rest_framework import serializers
from blog_api.models import Topic, Post, Comment

# Topic serializers


class TopicSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'title', 'description', 'prefers']

# Comment serializers


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'created_at', 'content', 'contains', 'author']

# Post serializers


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    created_at = serializers.DateField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'slug', 'title', 'text', 'created_at',
                  'updated_at', 'author', 'contains']
