from django.contrib import admin
from django.urls import path
from .views import PostViewSet, LikeUnlikeAPIView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', PostViewSet, basename='post')


urlpatterns = [path('like-unlike', LikeUnlikeAPIView.as_view(), name='like-unlike'),
]

urlpatterns += router.urls