from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RegistrationViewSet, UserActivityViewSet

router = DefaultRouter()
router.register('activity', UserActivityViewSet, basename='activity')
router.register('', RegistrationViewSet, basename='user')


urlpatterns = [
]

urlpatterns += router.urls