from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from api.serializers import UserSerializer
from api.permissions import IsSelfOrReadOnly
import json

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def social_sign_in(request):
    """
    Handle social sign-in.
    """
    provider = request.data.get('provider')
    token = request.data.get('token')
    # Here you would implement the logic to verify the social token
    # and create or authenticate the user accordingly.
    # This is just a placeholder response.
    return JsonResponse({'message': 'Social sign-in successful for provider: {}'.format(provider)}, status=200)

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def email_registration(request):
    """
    Handle email registration.
    """
    email = request.data.get('email')
    password = request.data.get('password')
    if not email or not password:
        return JsonResponse({'error': 'Email and password are required.'}, status=400)
    if User.objects.filter(email=email).exists():
        return JsonResponse({'error': 'Email is already in use.'}, status=400)
    user = User.objects.create(email=email, password=make_password(password))
    user.save()
    # Send OTP email logic goes here
    return JsonResponse({'message': 'User registered successfully. Please verify your email.'}, status=201)

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def email_verification(request):
    """
    Handle email verification with OTP.
    """
    email = request.data.get('email')
    otp = request.data.get('otp')
    # OTP verification logic goes here
    # This is just a placeholder response.
    return JsonResponse({'message': 'Email verified successfully.'}, status=200)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsSelfOrReadOnly])
def user_detail(request, pk):
    """
    Retrieve, update or delete a user instance.
    """
    try:
        user = get_object_or_404(User, pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)