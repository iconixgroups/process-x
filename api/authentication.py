from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework_jwt.settings import api_settings
from .models import UserProfile

jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER

class SocialAuthentication(BaseAuthentication):
    def authenticate(self, request):
        provider = request.data.get('provider')
        token = request.data.get('token')

        if provider is None or token is None:
            return None

        # Here you should add the logic to verify the social token with the provider
        # For example, using requests to send the token to the provider's token verification URL
        # If the token is valid, retrieve or create the user based on the provider's response

        try:
            # This is a placeholder for actual user retrieval/creation logic
            user = User.objects.get(username='social_user')
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        jwt_value = request.META.get('HTTP_AUTHORIZATION')

        if jwt_value is None:
            return None

        try:
            payload = jwt_decode_handler(jwt_value)
        except jwt.ExpiredSignature:
            raise exceptions.AuthenticationFailed('Token has expired')
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed('Error decoding token')

        username = jwt_get_username_from_payload(payload)

        if not username:
            raise exceptions.AuthenticationFailed('Invalid payload')

        try:
            user = User.objects.get_by_natural_key(username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, payload)

class EmailVerificationAuthentication(BaseAuthentication):
    def authenticate(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')

        if email is None or otp is None:
            return None

        # Here you should add the logic to verify the OTP with the stored one
        # If the OTP is valid, retrieve the user and return it

        try:
            user_profile = UserProfile.objects.get(user__email=email, otp=otp)
            user = user_profile.user
        except UserProfile.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user or wrong OTP')

        return (user, None)