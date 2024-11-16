import sys
sys.dont_write_bytecode = True
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuditLogViewSet

router = DefaultRouter()
router.register(r'logs', AuditLogViewSet, basename='audit_log')

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
]