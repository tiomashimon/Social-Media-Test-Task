from rest_framework import serializers
from .models import Post, DailyLikes
from ..user.serializers import UserSeralizer
from django.contrib.auth.models import User
from rest_framework.response import Response


class DailyLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLikes
        fields = '__all__'


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    likes = UserSeralizer(many=True, read_only=True)
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        

        return instance
        

        
