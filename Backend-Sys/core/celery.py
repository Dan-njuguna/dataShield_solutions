# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Susan\OneDrive\Desktop\datashield solutions\Backend-Sys\core\celery.py
# Compiled at: 2024-10-29 16:18:04
# Size of source mod 2**32: 238 bytes
import os
from celery import Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
app = Celery("your_project")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# okay decompiling celery.cpython-38.pyc
