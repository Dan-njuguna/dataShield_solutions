# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Susan\OneDrive\Desktop\datashield solutions\Backend-Sys\audit_log\urls.py
# Compiled at: 2024-10-29 17:28:20
# Size of source mod 2**32: 294 bytes
from django.urls import path
from . import views
urlpatterns = [
 path("logs/", (views.audit_log_list), name="audit_log_list"),
 path("logs/<slug:slug>/", (views.audit_log_detail), name="audit_log_detail"),
 path("logs/log_action/", (views.log_action_view), name="log_action")]

# okay decompiling urls.cpython-38.pyc
