from django.urls import path, include
from rest_framework import routers

from blog_api.api.resources import TopicCreateViewSet, TopicReadViewSet, PostReadViewSet, PostCreateViewSet

router = routers.SimpleRouter()
router.register(r'topics-create', TopicCreateViewSet)
router.register(r'topics-read', TopicReadViewSet)
router.register(r'posts-read', PostReadViewSet)
router.register(r'posts-create', PostCreateViewSet)

urlpatterns = [
    path('', include(router.urls))
]
