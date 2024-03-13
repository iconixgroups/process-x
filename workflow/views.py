from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Workflow
from .serializers import WorkflowSerializer
from django.shortcuts import get_object_or_404

class WorkflowView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = WorkflowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        workflow_id = kwargs.get('workflow_id')
        workflow = get_object_or_404(Workflow, pk=workflow_id)
        serializer = WorkflowSerializer(workflow, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        workflow_id = kwargs.get('workflow_id')
        workflow = get_object_or_404(Workflow, pk=workflow_id)
        workflow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WorkflowDetailView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        workflow_id = kwargs.get('workflow_id')
        workflow = get_object_or_404(Workflow, pk=workflow_id)
        serializer = WorkflowSerializer(workflow)
        return Response(serializer.data, status=status.HTTP_200_OK)