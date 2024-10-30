# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Susan\OneDrive\Desktop\datashield solutions\Backend-Sys\reporting\views.py
# Compiled at: 2024-10-29 15:34:40
# Size of source mod 2**32: 2528 bytes
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core import serializers
from .models import ScheduledReport, DataBreachReport, ComplianceAudit
from .forms import ScheduledReportForm, DataBreachReportForm, ComplianceAuditForm

def scheduled_report_list(request):
    reports = ScheduledReport.objects.all()
    data = serializers.serialize("json", reports)
    return JsonResponse(data, safe=False)


def scheduled_report_detail(request, id):
    report = get_object_or_404(ScheduledReport, id=id)
    data = serializers.serialize("json", [report])
    return JsonResponse(data, safe=False)


def data_breach_report_list(request):
    reports = DataBreachReport.objects.all()
    data = serializers.serialize("json", reports)
    return JsonResponse(data, safe=False)


def data_breach_report_detail(request, id):
    report = get_object_or_404(DataBreachReport, id=id)
    data = serializers.serialize("json", [report])
    return JsonResponse(data, safe=False)


def compliance_audit_list(request):
    audits = ComplianceAudit.objects.all()
    data = serializers.serialize("json", audits)
    return JsonResponse(data, safe=False)


def compliance_audit_detail(request, id):
    audit = get_object_or_404(ComplianceAudit, id=id)
    data = serializers.serialize("json", [audit])
    return JsonResponse(data, safe=False)


def create_scheduled_report(request):
    if request.method == "POST":
        form = ScheduledReportForm(request.POST)
        if form.is_valid():
            report = form.save()
            data = serializers.serialize("json", [report])
            return JsonResponse(data, status=201, safe=False)
        return JsonResponse({"error": "Invalid data"}, status=400)


def create_data_breach_report(request):
    if request.method == "POST":
        form = DataBreachReportForm(request.POST)
        if form.is_valid():
            report = form.save()
            data = serializers.serialize("json", [report])
            return JsonResponse(data, status=201, safe=False)
        return JsonResponse({"error": "Invalid data"}, status=400)


def create_compliance_audit(request):
    if request.method == "POST":
        form = ComplianceAuditForm(request.POST)
        if form.is_valid():
            audit = form.save()
            data = serializers.serialize("json", [audit])
            return JsonResponse(data, status=201, safe=False)
        return JsonResponse({"error": "Invalid data"}, status=400)

# okay decompiling views.cpython-38.pyc
