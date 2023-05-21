from rest_framework import viewsets
from blog_api.api.serializers import TopicSerializer, PostSerializer, CommentSerializer
from blog_api.models import Topic, Post, Comment

# Topic views


class TopicModelViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


# Post views


class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Comment views


class CommentModelViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

