from django.shortcuts import get_object_or_404, render
from .serializers import DailyLikesSerializer, PostSerializer, DailyLikesAnalyticsSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Post, DailyLikes
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins
from django.utils import timezone
from django.db.models import Sum



class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # permission_classes = [IsAuthenticated]



class LikeUnlikeAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    def put(self, request):
        post = get_object_or_404(Post, id=request.data.get('post'))
        user = get_object_or_404(User, id=request.data.get('user'))

        response = post.like_unlike(user)
        post.save()

        return Response({'response':response},status=200)


class DailyLikesViewSet(ModelViewSet):
    serializer_class = DailyLikesSerializer
    queryset = DailyLikes.objects.all()
    
    # permission_classes = [IsAuthenticated]



class DailyLikesAnalyticsViewSet(APIView):
    def get(self, request, *args, **kwargs):

        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')

        queryset = DailyLikes.objects.all()

        if date_from and date_to:
            queryset = queryset.filter(date__range=[date_from, date_to])

        total_likes = queryset.aggregate(TOTAL=Sum('likes_count'))['TOTAL']

        if not total_likes:
            total_likes = 0

        return Response({'total':total_likes})
