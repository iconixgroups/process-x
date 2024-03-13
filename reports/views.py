from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Report
from .serializers import ReportSerializer
from api.permissions import IsAdminOrReadOnly

class ReportList(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

    def get_queryset(self):
        """
        Optionally restricts the returned reports to a given module,
        by filtering against a `moduleId` query parameter in the URL.
        """
        queryset = self.queryset
        module_id = self.request.query_params.get('moduleId', None)
        if module_id is not None:
            queryset = queryset.filter(module__id=module_id)
        return queryset

class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

    def get_object(self):
        """
        Returns the object the view is displaying.
        You may want to override this if you need to provide non-standard queryset lookups.
        """
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj

class GenerateReport(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

    def get(self, request, *args, **kwargs):
        module_id = kwargs.get('moduleId', None)
        if not module_id:
            return Response({"message": "Module ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Logic to generate report data based on the module_id
        # This is a placeholder for the actual implementation
        report_data = {
            "moduleId": module_id,
            "dataSubmissions": 150,
            "statuses": {
                "pending": 50,
                "approved": 80,
                "rejected": 20
            }
        }

        return Response(report_data, status=status.HTTP_200_OK)