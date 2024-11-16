import sys
sys.dont_write_bytecode = True
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ScheduledReportViewSet, DataBreachReportViewSet, ComplianceAuditViewSet

router = DefaultRouter()
router.register(r'scheduled-reports', ScheduledReportViewSet, basename='scheduled-report')
router.register(r'data-breach-reports', DataBreachReportViewSet, basename='data-breach-report')
router.register(r'compliance-audits', ComplianceAuditViewSet, basename='compliance-audit')

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
]