from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .models import UserActivity
from .serializers import UserSeralizer, UserActivitySeralizer


class RegistrationViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSeralizer



class UserActivityViewSet(ModelViewSet):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySeralizer