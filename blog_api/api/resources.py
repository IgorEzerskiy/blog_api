from rest_framework import viewsets

from blog_api.api.serializers import TopicCreateSerializer, TopicReadSerializer, \
                                     PostReadSerializer, PostCreateSerializer, \
                                     CommentCreateSerializer, CommentReadSerializer
from blog_api.models import Topic, Post, Comment
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView

# Topic views


class TopicCreateAPIView(CreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicCreateSerializer


class TopicReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicReadSerializer


class TopicUpdateAPIView(UpdateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicCreateSerializer


class TopicDestroyAPIView(DestroyAPIView):
    queryset = Topic.objects.all()

# Post views


class PostReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostReadSerializer


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer


class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer


class PostDestroyAPIView(DestroyAPIView):
    queryset = Post.objects.all()

# Comment views


class CommentReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentReadSerializer


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer


class CommentUpdateAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer


class CommentDestroyAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
