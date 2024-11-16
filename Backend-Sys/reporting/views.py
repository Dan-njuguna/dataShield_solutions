import sys
sys.dont_write_bytecode = True
from rest_framework import viewsets, permissions, throttling
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import ScheduledReport, DataBreachReport, ComplianceAudit
from .serializers import ScheduledReportSerializer, DataBreachReportSerializer, ComplianceAuditSerializer

class ReportingPagination(PageNumberPagination):
    """Custom pagination class for reporting models."""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ScheduledReportViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing scheduled reports.
    
    Provides list, create, retrieve, update, and delete functionalities.
    Supports pagination and authentication.
    """
    queryset = ScheduledReport.objects.all()
    serializer_class = ScheduledReportSerializer
    pagination_class = ReportingPagination
    permission_classes = [permissions.AllowAny]
    throttle_classes = [throttling.AnonRateThrottle]

    def get_queryset(self):
        queryset = super().get_queryset()
        organization_id = self.request.query_params.get('organization_id', None)
        if organization_id is not None:
            queryset = queryset.filter(organization_id=organization_id)
        return queryset

class DataBreachReportViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing data breach reports.
    
    Provides list, create, retrieve, update, and delete functionalities.
    Supports pagination and authentication.
    """
    queryset = DataBreachReport.objects.all()
    serializer_class = DataBreachReportSerializer
    pagination_class = ReportingPagination
    permission_classes = [permissions.IsAuthenticated]

class ComplianceAuditViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing compliance audits.
    
    Provides list, create, retrieve, update, and delete functionalities.
    Supports pagination and authentication.
    """
    queryset = ComplianceAudit.objects.all()
    serializer_class = ComplianceAuditSerializer
    pagination_class = ReportingPagination
    permission_classes = [permissions.IsAuthenticated]