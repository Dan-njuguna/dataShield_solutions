
from django.urls import path
from .views import data_protection_regulation_list, data_protection_regulation_detail, compliance_status_list, compliance_status_detail, compliance_report_list, compliance_report_detail, compliance_document_list, compliance_document_detail, data_processing_activity_list, data_processing_activity_detail, dpi_a_list, dpi_a_detail, incident_list, incident_detail
urlpatterns = [
 path("data-protection-regulations/", data_protection_regulation_list, name="data_protection_regulation_list"),
 path("data-protection-regulations/<slug:slug>/", data_protection_regulation_detail, name="data_protection_regulation_detail"),
 path("compliance-status/", compliance_status_list, name="compliance_status_list"),
 path("compliance-status/<slug:slug>/", compliance_status_detail, name="compliance_status_detail"),
 path("compliance-reports/", compliance_report_list, name="compliance_report_list"),
 path("compliance-reports/<slug:slug>/", compliance_report_detail, name="compliance_report_detail"),
 path("compliance-documents/", compliance_document_list, name="compliance_document_list"),
 path("compliance-documents/<slug:slug>/", compliance_document_detail, name="compliance_document_detail"),
 path("data-processing-activities/", data_processing_activity_list, name="data_processing_activity_list"),
 path("data-processing-activities/<slug:slug>/", data_processing_activity_detail, name="data_processing_activity_detail"),
 path("dpias/", dpi_a_list, name="dpi_a_list"),
 path("dpias/<slug:slug>/", dpi_a_detail, name="dpi_a_detail"),
 path("incidents/", incident_list, name="incident_list"),
 path("incidents/<slug:slug>/", incident_detail, name="incident_detail")]


