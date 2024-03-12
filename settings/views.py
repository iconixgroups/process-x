from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Module
from .serializers import ModuleSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.permissions import IsAdminOrReadOnly

@api_view(['GET', 'POST'])
def module_list(request):
    """
    List all modules, or create a new module.
    """
    if request.method == 'GET':
        modules = Module.objects.all()
        serializer = ModuleSerializer(modules, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def module_detail(request, pk):
    """
    Retrieve, update or delete a module instance.
    """
    module = get_object_or_404(Module, pk=pk)
    if request.method == 'GET':
        serializer = ModuleSerializer(module)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ModuleSerializer(module, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        module.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def publish_module(request, pk):
    """
    Publish a module, making it accessible to users with appropriate permissions.
    """
    module = get_object_or_404(Module, pk=pk)
    if request.method == 'POST':
        module.published = True
        module.save(update_fields=['published'])
        return Response({'status': 'module published'}, status=status.HTTP_200_OK)