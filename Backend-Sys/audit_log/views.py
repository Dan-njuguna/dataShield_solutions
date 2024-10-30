# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Susan\OneDrive\Desktop\datashield solutions\Backend-Sys\audit_log\views.py
# Compiled at: 2024-10-29 15:07:04
# Size of source mod 2**32: 2118 bytes
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from .models import AuditLog
from .forms import AuditLogForm
import json

def audit_log_list(request):
    """View to list all audit logs."""
    logs = AuditLog.objects.all()
    log_data = [{'id':log.id, 
     'action':log.action, 
     'affected_resource':log.affected_resource, 
     'user':log.user.email if (log.user) else "System", 
     'organization':(log.organization).name, 
     'created_at':log.created_at, 
     'is_compliant':log.is_compliant, 
     'slug':log.slug} for log in logs]
    return JsonResponse({"logs": log_data}, safe=False)


def audit_log_detail(request, slug):
    """View to retrieve a specific audit log by slug."""
    try:
        log = AuditLog.objects.get(slug=slug)
        log_data = {'id':log.id, 
         'action':log.action, 
         'affected_resource':log.affected_resource, 
         'user':log.user.email if (log.user) else "System", 
         'organization':(log.organization).name, 
         'created_at':log.created_at, 
         'is_compliant':log.is_compliant, 
         'compliance_notes':log.compliance_notes, 
         'additional_data':log.additional_data}
        return JsonResponse({"log": log_data}, status=200)
    except AuditLog.DoesNotExist:
        raise Http404("Audit log not found")


@csrf_exempt
def log_action_view(request):
    """View to log a new action."""
    if request.method == "POST":
        data = json.loads(request.body)
        form = AuditLogForm(data)
        if form.is_valid():
            log_entry = form.save()
            return JsonResponse({'success':True,  'log_id':log_entry.id,  'slug':log_entry.slug}, status=201)
        return JsonResponse({'success':False,  'errors':form.errors}, status=400)
    return JsonResponse({'success':False,  'message':"Invalid request method."}, status=400)

# okay decompiling views.cpython-38.pyc
