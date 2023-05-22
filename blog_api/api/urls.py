from django.urls import path, include
from rest_framework import routers

from blog_api.api.resources import TopicModelViewSet, PostModelViewSet, CommentModelViewSet

router = routers.SimpleRouter()
router.register(r'topics', TopicModelViewSet)
router.register(r'posts', PostModelViewSet)
router.register(r'comments', CommentModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
