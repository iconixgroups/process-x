from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import UserSerializer
from user.models import User
from django.conf import settings

class RegisterUserAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            user_data['password'] = make_password(user_data['password'])
            user = User.objects.create(**user_data)
            # Send OTP email
            otp = User.generate_otp()
            user.otp = otp
            user.save()
            send_mail(
                subject="Verify Your Email",
                message=f"Your OTP is: {otp}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)