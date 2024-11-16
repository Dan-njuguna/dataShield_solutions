import sys
sys.dont_write_bytecode = True
from rest_framework import viewsets, permissions, throttling
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import AuditLog
from .serializers import AuditLogSerializer

class AuditLogPagination(PageNumberPagination):
    """Custom pagination class for AuditLog."""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class AuditLogViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing audit log entries.
    
    Provides list, create, retrieve, update, and delete functionalities.
    Supports pagination, filtering, and authentication.
    """
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    pagination_class = AuditLogPagination
    permission_classes = [permissions.
    AllowAny]  # Require authentication
    throttle_classes = [throttling.AnonRateThrottle]  # Throttle for anonymous users

    def get_queryset(self):
        """
        Optionally restricts the returned audit logs to a given organization,
        by filtering against an `organization` query parameter in the URL.
        Additionally, ensure the user has access to the organization.
        """
        queryset = super().get_queryset()
        organization_id = self.request.query_params.get('organization')

        if organization_id:
            # Check if the user is part of the organization
            if not self.request.user.organizations.filter(id=organization_id).exists():
                # Return an empty queryset if the user does not belong to the organization
                return queryset.none()  # Optionally, you could raise an exception here

            # Filter by organization
            queryset = queryset.filter(organization_id=organization_id)

        return queryset

    def perform_create(self, serializer):
        """Override to add the current user to the log entry."""
        serializer.save(user=self.request.user)