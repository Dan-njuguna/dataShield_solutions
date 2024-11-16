import sys
sys.dont_write_bytecode = True
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PolicyViewSet, PolicyVersionViewSet, ApprovalWorkflowViewSet

router = DefaultRouter()
router.register(r'policies', PolicyViewSet, basename='policy')
router.register(r'policy-versions', PolicyVersionViewSet, basename='policy-version')
router.register(r'approval-workflows', ApprovalWorkflowViewSet, basename='approval-workflow')

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
]