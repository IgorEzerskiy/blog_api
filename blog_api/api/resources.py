from rest_framework import viewsets

from blog_api.api.serializers import TopicCreateSerializer, TopicReadSerializer, PostReadSerializer, \
                                     PostCreateSerializer
from blog_api.models import Topic, Post


class TopicCreateViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicCreateSerializer


class TopicReadViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Topic.objects.all()
    serializer_class = TopicReadSerializer


class PostReadViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Post.objects.all()
    serializer_class = PostReadSerializer


class PostCreateViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
