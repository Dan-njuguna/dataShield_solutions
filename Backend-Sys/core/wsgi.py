# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Susan\OneDrive\Desktop\datashield solutions\Backend-Sys\core\wsgi.py
# Compiled at: 2024-10-24 02:35:37
# Size of source mod 2**32: 172 bytes
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
application = get_wsgi_application()

# okay decompiling wsgi.cpython-38.pyc
