from django.contrib import admin
from django.urls import path
from .views import PostViewSet, LikeUnlikeAPIView, DailyLikesViewSet, DailyLikesAnalyticsViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('', PostViewSet, basename='post')

daily_likes = DailyLikesViewSet.as_view({'get':'list', "post":'create'})


urlpatterns = [path('like-unlike/', LikeUnlikeAPIView.as_view(), name='like-unlike'),
               path('daily-likes/', daily_likes, name='daily-likes'),
                path('analitics/', DailyLikesAnalyticsViewSet.as_view(), name='daily-likes-analytics'),

]

urlpatterns += router.urls