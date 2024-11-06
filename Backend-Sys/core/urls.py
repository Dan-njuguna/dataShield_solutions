from django.contrib import admin
from django.urls import path,include

from django.views.generic import TemplateView

urlpatterns = [
    path("auth/", include("authentication.urls")),
    path('admin/', admin.site.urls),
    
    path("compliance/", include("compliance_management.urls")),
    path("policy/", include("policy_management.urls")),
    path("report/", include("reporting.urls")),
    path("audit/", include("audit_log.urls")),
    path("analytics/", include("analytics.urls")),
]
