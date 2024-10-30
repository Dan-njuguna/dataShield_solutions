
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
 path("admin/", admin.site.urls),
 path("compliance/", include("compliance_management.urls")),
 path("audit/", include("audit_log.urls")),
 path("reporting/", include("reporting.urls")),
 path("policy/", include("policy_management.urls")),
 path("auth/", include("authentication.urls")),
 ]


