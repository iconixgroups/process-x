from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from social_core.exceptions import AuthAlreadyAssociated, AuthException
from social_core.utils import social_strategy
from social_django.utils import load_strategy, load_backend

User = get_user_model()

class SocialSignInView(views.APIView):
    """
    View to handle social sign-in.
    """

    def post(self, request, *args, **kwargs):
        provider = request.data.get('provider')
        token = request.data.get('token')

        strategy = load_strategy(request)
        backend = load_backend(strategy=strategy, name=provider, redirect_uri=None)

        try:
            user = backend.do_auth(token)
        except AuthAlreadyAssociated:
            return Response({"detail": "This social account is already in use."}, status=status.HTTP_400_BAD_REQUEST)
        except AuthException as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        if user:
            if not user.is_active:
                return Response({"detail": "User account is disabled."}, status=status.HTTP_403_FORBIDDEN)

            refresh = RefreshToken.for_user(user)
            response_data = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                },
            }

            return Response(response_data, status=status.HTTP_200_OK)

        else:
            return Response({"detail": "Authentication Failed."}, status=status.HTTP_401_UNAUTHORIZED)

# Add URL patterns in your Django urls.py
# urlpatterns = [
#     path('auth/social', SocialSignInView.as_view(), name='social-sign-in'),
# ]