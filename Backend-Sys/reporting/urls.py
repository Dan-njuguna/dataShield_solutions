# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Susan\OneDrive\Desktop\datashield solutions\Backend-Sys\reporting\urls.py
# Compiled at: 2024-10-29 15:33:45
# Size of source mod 2**32: 986 bytes
from django.urls import path
from . import views
urlpatterns = [
 path("scheduled-reports/", (views.scheduled_report_list), name="scheduled_report_list"),
 path("scheduled-reports/<int:id>/", (views.scheduled_report_detail), name="scheduled_report_detail"),
 path("data-breach-reports/", (views.data_breach_report_list), name="data_breach_report_list"),
 path("data-breach-reports/<int:id>/", (views.data_breach_report_detail), name="data_breach_report_detail"),
 path("compliance-audits/", (views.compliance_audit_list), name="compliance_audit_list"),
 path("compliance-audits/<int:id>/", (views.compliance_audit_detail), name="compliance_audit_detail"),
 path("create-scheduled-report/", (views.create_scheduled_report), name="create_scheduled_report"),
 path("create-data-breach-report/", (views.create_data_breach_report), name="create_data_breach_report"),
 path("create-compliance-audit/", (views.create_compliance_audit), name="create_compliance_audit")]

# okay decompiling urls.cpython-38.pyc
