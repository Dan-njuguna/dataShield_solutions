import sys
sys.dont_write_bytecode = True
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DataProtectionRegulationViewSet,
    ComplianceStatusViewSet,
    ComplianceReportViewSet,
    ComplianceDocumentViewSet,
    DataProcessingActivityViewSet,
    DPIAViewSet,
    KenyaDPAViewSet,
    IncidentViewSet
)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'data-protection-regulations', DataProtectionRegulationViewSet, basename='data_protection_regulation')
router.register(r'KenyaDPA', KenyaDPAViewSet, basename='KenyaDPA')
router.register(r'compliance-status', ComplianceStatusViewSet, basename='compliance_status')
router.register(r'compliance-reports', ComplianceReportViewSet, basename='compliance_report')
router.register(r'compliance-documents', ComplianceDocumentViewSet, basename='compliance_document')
router.register(r'data-processing-activities', DataProcessingActivityViewSet, basename='data_processing_activity')
router.register(r'dpias', DPIAViewSet, basename='dpi_a')
router.register(r'incidents', IncidentViewSet, basename='incident')

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
]