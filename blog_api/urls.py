from django.urls import path, include

urlpatterns = [
    path('api/', include('blog_api.api.urls'))
]
