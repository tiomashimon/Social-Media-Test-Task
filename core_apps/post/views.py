from django.shortcuts import get_object_or_404, render
from .serializers import DailyLikesSerializer, PostSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Post
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]



class LikeUnlikeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request):
        post = get_object_or_404(Post, id=request.data.get('post'))
        user = get_object_or_404(User, id=request.data.get('user'))

        response = post.like_unlike(user)
        post.save()

        return Response({'response':response},status=200)


