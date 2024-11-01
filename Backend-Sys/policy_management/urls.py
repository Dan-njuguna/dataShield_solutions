# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Susan\OneDrive\Desktop\datashield solutions\Backend-Sys\policy_management\urls.py
# Compiled at: 2024-10-29 15:30:01
# Size of source mod 2**32: 956 bytes
from django.urls import path
from . import views
urlpatterns = [
 path("policies/", (views.policy_list), name="policy_list"),
 path("policies/<slug>/", (views.policy_detail), name="policy_detail"),
 path("policies/<slug>/versions/", (views.policy_version_list), name="policy_version_list"),
 path("policies/<slug>/versions/<int:version_number>/", (views.policy_version_detail), name="policy_version_detail"),
 path("policies/<slug>/approval-workflows/", (views.approval_workflow_list), name="approval_workflow_list"),
 path("policies/<slug>/approval-workflows/<int:id>/", (views.approval_workflow_detail), name="approval_workflow_detail"),
 path("create-policy/", (views.create_policy), name="create_policy"),
 path("policies/<slug>/create-version/", (views.create_policy_version), name="create_policy_version"),
 path("policies/<slug>/create-approval-workflow/", (views.create_approval_workflow), name="create_approval_workflow")]

# okay decompiling urls.cpython-38.pyc
