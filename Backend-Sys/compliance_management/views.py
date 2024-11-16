import sys
sys.dont_write_bytecode = True
from rest_framework import viewsets, permissions
from rest_framework.throttling import UserRateThrottle
from .models import (
    DataProtectionRegulation,
    ComplianceStatus,
    ComplianceReport,
    ComplianceDocument,
    DataProcessingActivity,
    DPIA,
    Incident,
    KenyaDPA
)
from .serializers import (
    DataProtectionRegulationSerializer,
    KenyaDPASerializer,
    ComplianceStatusSerializer,
    ComplianceReportSerializer,
    ComplianceDocumentSerializer,
    DataProcessingActivitySerializer,
    DPIASerializer,
    IncidentSerializer
)

class DataProtectionRegulationViewSet(viewsets.ModelViewSet):
    """ViewSet for managing data protection regulations."""
    queryset = DataProtectionRegulation.objects.all()
    serializer_class = DataProtectionRegulationSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [UserRateThrottle]  


class KenyaDPAViewSet(viewsets.ModelViewSet):
    """ViewSet for managing Kenya DPA."""
    queryset = KenyaDPA.objects.all().order_by('category')
    serializer_class = KenyaDPASerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        print('Response data:', response.data)
        return response

class ComplianceStatusViewSet(viewsets.ModelViewSet):
    """ViewSet for managing compliance statuses."""
    queryset = ComplianceStatus.objects.all()
    serializer_class = ComplianceStatusSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [UserRateThrottle]  

class ComplianceReportViewSet(viewsets.ModelViewSet):
    """ViewSet for managing compliance reports."""
    queryset = ComplianceReport.objects.all().order_by('generated_at')
    serializer_class = ComplianceReportSerializer
    permission_classes = [permissions.AllowAny]
    throttle_classes = [UserRateThrottle]  

class ComplianceDocumentViewSet(viewsets.ModelViewSet):
    """ViewSet for managing compliance documents."""
    queryset = ComplianceDocument.objects.all()
    serializer_class = ComplianceDocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [UserRateThrottle]  

class DataProcessingActivityViewSet(viewsets.ModelViewSet):
    """ViewSet for managing data processing activities."""
    queryset = DataProcessingActivity.objects.all()
    serializer_class = DataProcessingActivitySerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [UserRateThrottle]  

class DPIAViewSet(viewsets.ModelViewSet):
    """ViewSet for managing Data Protection Impact Assessments (DPIAs)."""
    queryset = DPIA.objects.all()
    serializer_class = DPIASerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [UserRateThrottle]  

class IncidentViewSet(viewsets.ModelViewSet):
    """ViewSet for managing incident reports."""
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [ UserRateThrottle]  

