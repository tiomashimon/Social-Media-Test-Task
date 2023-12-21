from .models import UserActivity
from django.utils import timezone


class UserRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        user = request.user if request.user.is_authenticated else None

        if user:
            user_activity = UserActivity.objects.filter(user=user).first()
            if user_activity:
                user_activity.last_request_time = timezone.now()
                user_activity.save()

        return response
