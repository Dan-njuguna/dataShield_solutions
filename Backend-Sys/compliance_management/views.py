
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.core import serializers
from .models import DataProtectionRegulation, ComplianceStatus, ComplianceReport, ComplianceDocument, DataProcessingActivity, DPIA, Incident
from .forms import DataProtectionRegulationForm, ComplianceStatusForm, ComplianceReportForm, ComplianceDocumentForm, DataProcessingActivityForm, DPIAForm, IncidentForm

def data_protection_regulation_list(request):
    regulations = DataProtectionRegulation.objects.all()
    data = serializers.serialize("json", regulations)
    return JsonResponse(data, safe=False)


def data_protection_regulation_detail(request, slug):
    regulation = get_object_or_404(DataProtectionRegulation, slug=slug)
    data = serializers.serialize("json", [regulation])
    return JsonResponse(data, safe=False)


def compliance_status_list(request):
    statuses = ComplianceStatus.objects.all()
    data = serializers.serialize("json", statuses)
    return JsonResponse(data, safe=False)


def compliance_status_detail(request, slug):
    status = get_object_or_404(ComplianceStatus, slug=slug)
    data = serializers.serialize("json", [status])
    return JsonResponse(data, safe=False)


def compliance_report_list(request):
    reports = ComplianceReport.objects.all()
    data = serializers.serialize("json", reports)
    return JsonResponse(data, safe=False)


def compliance_report_detail(request, slug):
    report = get_object_or_404(ComplianceReport, slug=slug)
    data = serializers.serialize("json", [report])
    return JsonResponse(data, safe=False)


def compliance_document_list(request):
    documents = ComplianceDocument.objects.all()
    data = serializers.serialize("json", documents)
    return JsonResponse(data, safe=False)


def compliance_document_detail(request, slug):
    document = get_object_or_404(ComplianceDocument, slug=slug)
    data = serializers.serialize("json", [document])
    return JsonResponse(data, safe=False)


def data_processing_activity_list(request):
    activities = DataProcessingActivity.objects.all()
    data = serializers.serialize("json", activities)
    return JsonResponse(data, safe=False)


def data_processing_activity_detail(request, slug):
    activity = get_object_or_404(DataProcessingActivity, slug=slug)
    data = serializers.serialize("json", [activity])
    return JsonResponse(data, safe=False)


def dpi_a_list(request):
    dpias = DPIA.objects.all()
    data = serializers.serialize("json", dpias)
    return JsonResponse(data, safe=False)


def dpi_a_detail(request, slug):
    dpi_a = get_object_or_404(DPIA, slug=slug)
    data = serializers.serialize("json", [dpi_a])
    return JsonResponse(data, safe=False)


def incident_list(request):
    incidents = Incident.objects.all()
    data = serializers.serialize("json", incidents)
    return JsonResponse(data, safe=False)


def incident_detail(request, slug):
    incident = get_object_or_404(Incident, slug=slug)
    data = serializers.serialize("json", [incident])
    return JsonResponse(data, safe=False)


@csrf_exempt
def create_data_protection_regulation(request):
    if request.method == "POST":
        form = DataProtectionRegulationForm(request.POST)
        if form.is_valid():
            regulation = form.save()
            data = serializers.serialize("json", [regulation])
            return JsonResponse(data, status=201, safe=False)
        return JsonResponse({"error": "Invalid data"}, status=400)


@csrf_exempt
def create_compliance_status(request):
    if request.method == "POST":
        form = ComplianceStatusForm(request.POST)
        if form.is_valid():
            status = form.save()
            data = serializers.serialize("json", [status])
            return JsonResponse(data, status=201, safe=False)
        return JsonResponse({"error": "Invalid data"}, status=400)


@csrf_exempt
def create_compliance_report(request):
    if request.method == "POST":
        form = ComplianceReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save()
            data = serializers.serialize("json", [report])
            return JsonResponse(data, status=201, safe=False)
        return JsonResponse({"error": "Invalid data"}, status=400)


@csrf_exempt
def create_compliance_document(request):
    if request.method == "POST":
        form = ComplianceDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            data = serializers.serialize("json", [document])
            return JsonResponse(data, status=201, safe=False)
        return JsonResponse({"error": "Invalid data"}, status=400)


@csrf_exempt
def create_data_processing_activity(request):
    if request.method == "POST":
        form = DataProcessingActivityForm(request.POST)
        if form.is_valid():
            activity = form.save()
            data = serializers.serialize("json", [activity])
            return JsonResponse(data, status=201, safe=False)
        return JsonResponse({"error": "Invalid data"}, status=400)


@csrf_exempt
def create_dpi_a(request):
    if request.method == "POST":
        form = DPIAForm(request.POST)
        if form.is_valid():
            dpi_a = form.save()
            data = serializers.serialize("json", [dpi_a])
            return JsonResponse(data, status=201, safe=False)
        return JsonResponse({"error": "Invalid data"}, status=400)


@csrf_exempt
def create_incident(request):
    if request.method == "POST":
        form = IncidentForm(request.POST)
        if form.is_valid():
            incident = form.save()
            data = serializers.serialize("json", [incident])
            return JsonResponse(data, status=201, safe=False)
        return JsonResponse({"error": "Invalid data"}, status=400)


