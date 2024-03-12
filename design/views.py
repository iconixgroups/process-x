from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Process, Form, Workflow
from .serializers import ProcessSerializer, FormSerializer, WorkflowSerializer
from api.permissions import IsCompanyAdmin

class ProcessDesignView(views.APIView):
    permission_classes = [IsAuthenticated, IsCompanyAdmin]

    def post(self, request, *args, **kwargs):
        serializer = ProcessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FormCreationView(views.APIView):
    permission_classes = [IsAuthenticated, IsCompanyAdmin]

    def post(self, request, *args, **kwargs):
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkflowCreationView(views.APIView):
    permission_classes = [IsAuthenticated, IsCompanyAdmin]

    def post(self, request, *args, **kwargs):
        serializer = WorkflowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)