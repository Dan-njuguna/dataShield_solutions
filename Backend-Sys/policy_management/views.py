# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Susan\OneDrive\Desktop\datashield solutions\Backend-Sys\policy_management\views.py
# Compiled at: 2024-10-29 15:28:28
# Size of source mod 2**32: 3046 bytes
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core import serializers
from .models import Policy, PolicyVersion, ApprovalWorkflow
from .forms import PolicyForm, PolicyVersionForm, ApprovalWorkflowForm

def policy_list(request):
    policies = Policy.objects.all()
    data = serializers.serialize("json", policies)
    return JsonResponse(data, safe=False)


def policy_detail(request, slug):
    policy = get_object_or_404(Policy, slug=slug)
    data = serializers.serialize("json", [policy])
    return JsonResponse(data, safe=False)


def policy_version_list(request, slug):
    policy = get_object_or_404(Policy, slug=slug)
    versions = policy.versions.all()
    data = serializers.serialize("json", versions)
    return JsonResponse(data, safe=False)


def policy_version_detail(request, slug, version_number):
    policy = get_object_or_404(Policy, slug=slug)
    version = get_object_or_404(PolicyVersion, policy=policy, version_number=version_number)
    data = serializers.serialize("json", [version])
    return JsonResponse(data, safe=False)


def approval_workflow_list(request, slug):
    policy = get_object_or_404(Policy, slug=slug)
    workflows = policy.approval_workflows.all()
    data = serializers.serialize("json", workflows)
    return JsonResponse(data, safe=False)


def approval_workflow_detail(request, slug, id):
    policy = get_object_or_404(Policy, slug=slug)
    workflow = get_object_or_404(ApprovalWorkflow, policy=policy, id=id)
    data = serializers.serialize("json", [workflow])
    return JsonResponse(data, safe=False)


def create_policy(request):
    if request.method == "POST":
        form = PolicyForm(request.POST)
        if form.is_valid():
            policy = form.save()
            data = serializers.serialize("json", [policy])
            return JsonResponse(data, status=201, safe=False)
        return JsonResponse({"error": "Invalid data"}, status=400)


def create_policy_version(request, slug):
    if request.method == "POST":
        policy = get_object_or_404(Policy, slug=slug)
        form = PolicyVersionForm(request.POST, request.FILES)
        if form.is_valid():
            version = form.save(commit=False)
            version.policy = policy
            version.save()
            data = serializers.serialize("json", [version])
            return JsonResponse(data, status=201, safe=False)
        return JsonResponse({"error": "Invalid data"}, status=400)


def create_approval_workflow(request, slug):
    if request.method == "POST":
        policy = get_object_or_404(Policy, slug=slug)
        form = ApprovalWorkflowForm(request.POST)
        if form.is_valid():
            workflow = form.save(commit=False)
            workflow.policy = policy
            workflow.save()
            data = serializers.serialize("json", [workflow])
            return JsonResponse(data, status=201, safe=False)
        return JsonResponse({"error": "Invalid data"}, status=400)


