from django.urls import path, include
from rest_framework import routers

from blog_api.api.resources import TopicCreateAPIView, TopicReadViewSet, TopicDestroyAPIView, TopicUpdateAPIView, \
                                    PostReadViewSet, PostCreateAPIView, PostDestroyAPIView, PostUpdateAPIView, \
                                    CommentReadViewSet, CommentCreateAPIView, CommentDestroyAPIView, CommentUpdateAPIView

router = routers.SimpleRouter()
router.register(r'topics-read', TopicReadViewSet)
router.register(r'posts-read', PostReadViewSet)
router.register(r'comments-read', CommentReadViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('post-create/', PostCreateAPIView.as_view()),
    path('post-update/<int:pk>', PostUpdateAPIView.as_view()),
    path('post-delete/<int:pk>', PostDestroyAPIView.as_view()),
    path('topic-create/', TopicCreateAPIView.as_view()),
    path('topic-update/<int:pk>', TopicUpdateAPIView.as_view()),
    path('topic-delete/<int:pk>', TopicDestroyAPIView.as_view()),
    path('comment-create/', CommentCreateAPIView.as_view()),
    path('comment-update/<int:pk>', CommentUpdateAPIView.as_view()),
    path('comment-delete/<int:pk>', CommentDestroyAPIView.as_view()),
]
