from rest_framework import serializers
from django.contrib.auth.models import User
from blog_api.models import Topic, Post, Comment

# Topic serializers


class TopicCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['title', 'description', 'prefers']


class TopicReadSerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)

    class Meta:
        model = Topic
        fields = ['title', 'description', 'prefers']

# Comment serializers


class CommentCreateSerializer(serializers.ModelSerializer):
    created_at = serializers.DateField(read_only=True)

    class Meta:
        model = Comment
        fields = ['created_at', 'content', 'contains', 'author']


class CommentReadSerializer(serializers.ModelSerializer):
    created_at = serializers.DateField(read_only=True)
    content = serializers.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = ['created_at', 'content', 'contains', 'author']

# Post serializers


class PostCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    created_at = serializers.DateField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields = ['slug', 'title', 'text', 'created_at',
                  'updated_at', 'author', 'contains']


class PostReadSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    title = serializers.CharField(read_only=True)
    text = serializers.CharField(read_only=True)
    created_at = serializers.DateField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'slug', 'title', 'text', 'created_at',
                  'updated_at', 'author', 'contains']
