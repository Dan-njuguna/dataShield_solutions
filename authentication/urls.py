from django.urls import path
from . import views

urlpatterns = [
 path("register/user/", (views.user_register), name="user_register"),
 path("register/organization/", (views.organization_register), name="organization_register"),
 path("login/", (views.user_login), name="user_login"),
 path("users/", (views.user_list), name="user_list"),
 path("organizations/", (views.organization_list), name="organization_list")]