# decompyle3 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Susan\OneDrive\Desktop\datashield solutions\Backend-Sys\authentication\urls.py
# Compiled at: 2024-10-29 14:58:51
# Size of source mod 2**32: 433 bytes
from django.urls import path
from . import views
urlpatterns = [
 path("register/user/", (views.user_register), name="user_register"),
 path("register/organization/", (views.organization_register), name="organization_register"),
 path("login/", (views.user_login), name="user_login"),
 path("users/", (views.user_list), name="user_list"),
 path("organizations/", (views.organization_list), name="organization_list")]

# okay decompiling urls.cpython-38.pyc
