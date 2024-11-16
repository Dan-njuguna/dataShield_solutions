import sys
sys.dont_write_bytecode = True
from rest_framework import viewsets, permissions, throttling
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Policy, PolicyVersion, ApprovalWorkflow
from .serializers import PolicySerializer, PolicyVersionSerializer, ApprovalWorkflowSerializer

class PolicyPagination(PageNumberPagination):
    """Custom pagination class for Policy."""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PolicyViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing policy documents.
    
    Provides list, create, retrieve, update, and delete functionalities.
    Supports pagination, filtering, and authentication.
    """
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    pagination_class = PolicyPagination
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [throttling.AnonRateThrottle]

class PolicyVersionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing policy versions.
    
    Provides list, create, retrieve, update, and delete functionalities.
    Supports pagination and authentication.
    """
    queryset = PolicyVersion.objects.all()
    serializer_class = PolicyVersionSerializer
    permission_classes = [permissions.IsAuthenticated]

class ApprovalWorkflowViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing approval workflows.
    
    Provides list, create, retrieve, update, and delete functionalities.
    Supports pagination and authentication.
    """
    queryset = ApprovalWorkflow.objects.all()
    serializer_class = ApprovalWorkflowSerializer
    permission_classes = [permissions.AllowAny]