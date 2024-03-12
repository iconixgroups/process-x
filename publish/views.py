from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Module
from .serializers import ModuleSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def publish_module(request, moduleId):
    """
    Publish a module, making it accessible to users with appropriate permissions.
    """
    try:
        module = Module.objects.get(id=moduleId, created_by=request.user)
    except Module.DoesNotExist:
        return Response({'message': 'Module does not exist'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ModuleSerializer(module, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save(published=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)