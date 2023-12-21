from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RegistrationViewSet, UserActivityViewSet
from django.contrib.auth.views import LogoutView


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView)

router = DefaultRouter()
router.register('activity', UserActivityViewSet, basename='activity')


Registration = RegistrationViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'
    }
)



urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/logout/', LogoutView.as_view, name='token_logout'),
    path('', Registration, name='user'),
    path('<int:pk>/', RegistrationViewSet.as_view({'get':'retrieve'}, name='user-detail'))
]

urlpatterns += router.urls