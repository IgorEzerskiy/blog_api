from rest_framework import viewsets, permissions
from blog_api.api.serializers import TopicSerializer, PostSerializer, CommentSerializer
from blog_api.models import Topic, Post, Comment
from django.contrib.auth.models import User
from blog_api.api.paginations import SmallPagePagination, LargePagePagination

# Topic views


class TopicModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    pagination_class = SmallPagePagination

# Post views


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = SmallPagePagination

    def perform_create(self, serializer):
        serializer.save(author=User.objects.get(id=self.request.user.id))

# Comment views


class CommentModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = LargePagePagination

    def perform_create(self, serializer):
        serializer.save(author=User.objects.get(id=self.request.user.id))
